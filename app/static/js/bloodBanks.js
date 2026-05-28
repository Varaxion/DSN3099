document.addEventListener('DOMContentLoaded', function() {
    const stateSelect = document.getElementById('state-select');
    const cityInput = document.getElementById('city-input');
    const searchBtn = document.getElementById('search-btn');
    const resultsContainer = document.getElementById('results-container');
    const noResults = document.getElementById('no-results');

    // Utility: show message
    function showErrorMessage(msg) {
        resultsContainer.innerHTML = `<div class="error-message"><p>${escapeHtml(msg)}</p></div>`;
    }
    function escapeHtml(s) {
        return String(s).replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;');
    }

    // Load states
    fetch('/getStates')
        .then(r => r.json())
        .then(states => {
            stateSelect.innerHTML = '<option value="">-- Select a State --</option>';
            states.forEach(s => {
                const o = document.createElement('option');
                o.value = s;
                o.textContent = s;
                stateSelect.appendChild(o);
            });
        })
        .catch(err => {
            console.error('Failed to load states', err);
        });

    // suggestion box for cities
    const suggestionBox = document.createElement('div');
    suggestionBox.className = 'suggestion-box';
    cityInput.parentNode.appendChild(suggestionBox);
    suggestionBox.style.display = 'none';

    async function fetchCitiesForState(state) {
        if (!state) return [];
        try {
            const res = await fetch(`/getCities?state=${encodeURIComponent(state)}`);
            if (!res.ok) return [];
            return await res.json();
        } catch (err) {
            console.error('getCities failed', err);
            return [];
        }
    }

    // city input autocomplete (startsWith suggestions)
    let latestCities = [];
    cityInput.addEventListener('input', async () => {
        const q = cityInput.value.trim();
        suggestionBox.innerHTML = '';

        const state = stateSelect.value;
        if (!state || q.length < 1) {
            suggestionBox.style.display = 'none';
            return;
        }

        // if we don't yet have cached cities for current state, fetch them
        if (!latestCities._forState || latestCities._forState !== state) {
            latestCities = await fetchCitiesForState(state);
            latestCities._forState = state;
        }

        const matches = latestCities.filter(c => c.toLowerCase().startsWith(q.toLowerCase())).slice(0, 8);
        if (matches.length === 0) {
            suggestionBox.style.display = 'none';
            return;
        }

        matches.forEach(m => {
            const item = document.createElement('div');
            item.className = 'suggestion-item';
            item.textContent = m;
            item.addEventListener('click', () => {
                cityInput.value = m;
                suggestionBox.style.display = 'none';
            });
            suggestionBox.appendChild(item);
        });
        suggestionBox.style.display = 'block';
    });

    document.addEventListener('click', e => {
        if (!suggestionBox.contains(e.target) && e.target !== cityInput) suggestionBox.style.display = 'none';
    });

    // spinner element
    function makeSpinner() {
        const sp = document.createElement('div');
        sp.className = 'loading-spinner';
        sp.innerHTML = `<div class="spinner"></div><p>Searching...</p>`;
        return sp;
    }

    // helper to sanitize contact and build tel link
    function telFor(contact) {
        if (!contact) return null;
        // keep digits and plus
        const cleaned = String(contact).replace(/[^\d+]/g, '');
        if (cleaned.length < 6) return null;
        return `tel:${cleaned}`;
    }

    // run search
    searchBtn.addEventListener('click', async () => {
        resultsContainer.innerHTML = '';
        noResults.style.display = 'none';

        const state = stateSelect.value.trim();
        const city = cityInput.value.trim();
        if (!state || !city) {
            alert('Please select a state and enter a city.');
            return;
        }

        const spinner = makeSpinner();
        resultsContainer.appendChild(spinner);

        try {
            const resp = await fetch('/searchBloodBanks', {
                method: 'POST',
                headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                body: `state=${encodeURIComponent(state)}&city=${encodeURIComponent(city)}`
            });

            const json = await resp.json().catch(() => null);
            resultsContainer.removeChild(spinner);

            if (!resp.ok) {
                // show server-provided error if present
                const msg = (json && (json.error || JSON.stringify(json))) || `Server error (${resp.status})`;
                // if suggestions provided, show them
                if (json && json.suggestions) {
                    const sugHtml = json.suggestions.map(s => `<button class="suggestion-sbtn">${escapeHtml(s)}</button>`).join(' ');
                    resultsContainer.innerHTML = `<div class="error-message"><p>${escapeHtml(msg)}</p><div class="suggestions-row">${sugHtml}</div></div>`;
                    // attach click handlers for suggestions to fill cityInput
                    document.querySelectorAll('.suggestion-sbtn').forEach(b => {
                        b.addEventListener('click', () => {
                            cityInput.value = b.textContent;
                        });
                    });
                } else {
                    showErrorMessage(msg);
                }
                return;
            }

            if (!Array.isArray(json) || json.length === 0) {
                noResults.style.display = 'block';
                noResults.textContent = 'No blood banks found for this city.';
                return;
            }

            json.forEach(item => {
                const card = document.createElement('div');
                card.className = 'blood-bank-card';

                // Properly access the fields using original case
                const name = item.Name || 'N/A';
                const address = item.Address || 'N/A';
                const cityName = item.City || city;
                const contact = item.Contact || 'N/A';

                // Move tel creation inside the card creation
                const tel = telFor(contact);
                
                card.innerHTML = `
                    <h3>${escapeHtml(name)}</h3>
                    <p><strong>Address:</strong> ${escapeHtml(address)}</p>
                    <p><strong>Contact:</strong> ${escapeHtml(contact)}</p>
                    <div class="card-actions">
                        <button class="copy-btn" data-copy="${escapeHtml(address)}">
                            📋 Copy Address
                        </button>
                        ${tel ? 
                            `<a href="${tel}" class="call-btn">📞 Call </a>` : 
                            `<button class="copy-btn" data-copy="${escapeHtml(contact)}">📋 Copy Contact</button>`
                        }
                    </div>
                    <p class="meta"><strong>City:</strong> ${escapeHtml(cityName)}</p>
                `;

                resultsContainer.appendChild(card);
            });
                        
            // wire up copy buttons
            document.querySelectorAll('.copy-btn').forEach(btn => {
                btn.addEventListener('click', async () => {
                    const text = btn.getAttribute('data-copy');
                    try {
                        await navigator.clipboard.writeText(text);
                        const old = btn.textContent;
                        btn.textContent = '✅ Copied';
                        setTimeout(() => btn.textContent = old, 1400);
                    } catch (err) {
                        console.error('Copy failed', err);
                    }
                });
            });
        } catch (err) {
            console.error('Unexpected error', err);
            resultsContainer.removeChild(spinner);
            showErrorMessage('Unexpected error occurred. See console for details.');
        }
    });
});
