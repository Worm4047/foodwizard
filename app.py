from flask import Flask
from flask_ask import Ask, statement, question, session
import json
import requests
import time
from stepsFromName import *
from readRecipeSteps import *
from readSearchResults import *
from searchDishesByName import *

app = Flask(__name__)
ask = Ask(app, "/")

@app.route('/')
def homepage():
    return "hi there, how ya doin?"

@ask.launch
def start_skill():
    welcome_message = 'Hello there, what would you like to make today ?'
    return question(welcome_message)

@ask.intent("searchdish",mapping={'dishname': "DishName"})
def search_dish(dishname):
    print "Inside search_dish",
    l = search(dishname)
    print l
    return statement(dishname+" Searched successfully")

@ask.intent('listenresults')
def listen_results():
    print 'Inside listen_results'
    return statement('results')

@ask.intent('getstepsofdish',mapping={'dishname':'DishName'})
def get_steps_of_dish(dishname):
    print 'Inside get steps for dish'
    print dishname
    l=1
    l = getSteps(dishname)
    retStr =" Steps found.Would you like to hear them out ?"
    return statement(retStr)

@ask.intent('nextstep')
def next_step():
    print 'inside next step'
    return statement('next step')

@ask.intent('previousstep')
def next_step():
    print 'inside previous step'
    return statement('previous step')

@ask.intent('nstep')
def n_step():
    print 'inside nth step'
    return statement('n step')


if __name__ == '__main__':
    app.run(debug=True)