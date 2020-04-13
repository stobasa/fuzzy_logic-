import os
from risk_c import risk_guage
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.exceptions import BadRequestKeyError

app = Flask(__name__)



@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == "POST":
        try:
            DD = int(request.form["DD"])
            DC = int(request.form["DC"])
            USM = int(request.form['USM'])
            ABP = int(request.form['ABP'])
            NBP = int(request.form['NBP'])
            APS = int(request.form['APS'])
            EII = int(request.form['EII'])
            EIP = int(request.form['EIP'])
            LPS = int(request.form['LPS'])
            IAS = int(request.form['IAS'])
            UIC = int(request.form['UIC'])
            FF = int(request.form['FF'])
            FO = int(request.form['FO'])
            ND = int(request.form['ND'])

            #print(structure_input, climate_input)
            risk_G = risk_guage(DD,DC,USM,ABP,NBP,APS,EII,EIP,LPS,IAS,UIC,FF,FO,ND)
            #return '<h1>{}</h1>'.format(risk_G)
            return render_template('test.html').format(risk_G)
        except Exception:
            return render_template('input.html').format("Input Values Between 1 to 10")
        


    return render_template('input.html').format(" ")

@app.route('/home', methods=['POST', 'GET'])
def input():
    if request.method == "POST":

        DD = int(request.form["DD"])
        DC = int(request.form["DC"])
        USM = int(request.form['USM'])
        ABP = int(request.form['ABP'])
        NBP = int(request.form['NBP'])
        APS = int(request.form['APS'])
        EII = int(request.form['EII'])
        EIP = int(request.form['EIP'])
        LPS = int(request.form['LPS'])
        IAS = int(request.form['IAS'])
        UIC = int(request.form['UIC'])
        FF = int(request.form['FF'])
        FO = int(request.form['FO'])
        ND = int(request.form['ND'])

        risk_G = risk_guage(DD,DC,USM,ABP,NBP,APS,EII,EIP,LPS,IAS,UIC,FF,FO,ND)
        return redirect(url_for("test.html", risk=risk_G))
    

@app.route("/result")
def result(risk):
    return f"<h1>{risk}</h1>"

if __name__ == "__main__":
    app.run(debug=True)
