from flask import Flask, render_template, request, redirect, url_for, flash
import SourceCode.rainfall_analysis as rainfall_analysis

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
            mae, score = rainfall_analysis.predict_rainfall(year, region)
            return render_template('rainfall_result.html', Mae=mae, Score=score)
    else:
        return redirect(url_for('rainfall_entry'))


if __name__ == '__main__':
    app.run(debug=True)
