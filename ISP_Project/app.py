from cgitb import html
from flask import Flask,render_template,url_for,request,redirect, make_response
import random
import json
from time import time
from random import random
from flask import Flask, render_template, make_response
app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def main():
    return render_template('index.html')

@app.route('/image.html')
def first():
    return(render_template("image.html"))

@app.route('/node2.html')  
def third():
    return(render_template("node2.html"))   

@app.route('/node3.html')  
def fourth():
    return(render_template("node3.html"))   


@app.route('/index.html')
def second():
    return(render_template("index.html"))   
  

@app.route('/data', methods=["GET", "POST"])
def data():
    # Data Format
    # [TIME, Temperature, Humidity, CO2, MQTT]

    Temperature = random() * 50
    Humidity = random() * 100
    CO2 = random() * 1000
    MQTT = random() * 1000
    

    data = [time() * 1000, Temperature, Humidity, CO2, MQTT]

    response = make_response(json.dumps(data))

    response.content_type = 'application/json'

    return response


if __name__ == "__main__":
    app.run(debug=True)