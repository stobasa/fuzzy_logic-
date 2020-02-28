import os
from risk import risk_guage
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)



@app.route('/')
def home():
    return render_template('input.html')

@app.route('/input', methods=['POST'])
def input():
    if request.method == "POST":
        structure_input = request.form["sturcture_input"]
        climate_input = request.form["climate_input"]
        risk_G = risk_guage(structure_input, climate_input)
        #return redirect(url_for("results", result=risk_G))
        return risk_G
    else:
        return render_template('input.html')
    

    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
