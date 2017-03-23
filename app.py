from flask import Flask
from flask_ask import Ask, statement, question, session
import json
import requests
import time
import unidecode
from utility import *

app = Flask(__name__)
ask = Ask(app, "/")

@app.route('/')
def homepage():
    return "hi there, how ya doin?"

@ask.launch
def start_skill():
    welcome_message = 'Hello there, hwhat would you like to make today ?'
    return question(welcome_message)

@ask.intent("searchdish",mapping={'dishname': "DishName"})
def search_dish(dishname):
    print "Inside search_dish",
    return statement(dishname+" Searched successfully")

if __name__ == '__main__':
    app.run(debug=True)