import sys
import os

# Add the project directory to the Python path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# Import the function from rainfall_analysis.py
from rainfall_analysis import predict_rainfall

from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = '5791628bb0b13ce0c676dfde280ba245'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/rainfall')
def rainfall():
    return render_template('rainfall.html')

@app.route('/rainfall_entry')
def rainfall_entry():
    return render_template('rainfall_entry.html')

@app.route('/rainfall_result', methods=['POST', 'GET'])
def rainfall_result():
    if request.method == 'POST':
        if len(request.form['Year']) == 0:
            flash("Please Enter Data!!")
            return redirect(url_for('rainfall_entry'))
        else:
            year = request.form['Year']
            region = request.form['SEL']
            mae, score = predict_rainfall(year, region)
            return render_template('rainfall_result.html', Mae=mae, Score=score)
    else:
        return redirect(url_for('rainfall_entry'))

@app.route('/emergency_contacts')
def emergency_contacts():
    return render_template('emergency_contacts.html')

@app.route('/Blood')
def Blood():
    return render_template('Blood.html')

@app.route('/sop')
def sop():
    return render_template('sop.html')

if __name__ == '__main__':
    app.run(debug=True)