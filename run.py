import os
from risk import risk_guage
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)



@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == "POST":
        structure_input = request.form["sturcture_input"]
        climate_input = request.form["climate_input"]

        print(structure_input, climate_input)
        risk_G = risk_guage(int(structure_input), int(climate_input))
        #return '<h1>{}</h1>'.format(risk_G)
        return render_template('test.html').format(structure_input, climate_input ,risk_G)


    return render_template('input.html')

@app.route('/home', methods=['POST', 'GET'])
def input():
    if request.method == "POST":
        structure_input = request.form["sturcture_input"]
        climate_input = request.form["climate_input"]
        risk_G = risk_guage(int(structure_input), int(climate_input))
        return redirect(url_for("result", risk=risk_G))
    

@app.route("/result")
def result(risk):
    return f"<h1>{risk}</h1>"

if __name__ == "__main__":
    app.run(debug=True)
