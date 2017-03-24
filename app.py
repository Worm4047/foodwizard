from flask import Flask
from flask_ask import Ask, statement, question, session
import json
import requests
import time
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from stepsFromName import *
from readRecipeSteps import *
from readSearchResults import *
from searchDishesByName import *
import ing_dish_from
from getcategorydishnames import *
import searchedDishIngredients as ingFunc
try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

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
    print "Inside search_dish",dishname
    l = getDishesByName(dishname)
    print l
    return question(dishname+" Searched successfully, would you like to hear results ?")

@ask.intent('listenresults')
def listen_results():
    print 'Inside listen_results'
    res = returnResults('dishsearchresult.txt')
    print res
    return statement(res)

@ask.intent('getstepsofdish',mapping={'dishname':'DishName'})
def get_steps_of_dish(dishname):
    print 'Inside get steps for dish'
    print dishname
    l=1
    l = getSteps(dishname)
    print l
    retStr =" Steps found.Would you like to hear them out ?"
    editHtmlFile(dishname)
    return statement(retStr)

@ask.intent('nextstep')
def next_step():
    print 'inside next step'
    step=readNext('recipeSteps.txt')
    print step
    return statement(step)

@ask.intent('previousstep')
def previous_step():
    print 'inside previous step'
    step=readPrev('recipeSteps.txt')
    print step
    return statement(step)

@ask.intent('nstep',mapping={'nvalue':'nValue'})
def n_step(nvalue):
    li2=['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th']
    li1=['first','second','third','fourth','fifth','sixth','seventh','eigth','ninth','tenth']
    print 'inside nth step'
    if nvalue not in li1:
        ind=li2.index(nvalue)
    else:
        ind=li1.index(nvalue)
            
    step=readNthLine('recipeSteps.txt',ind)
    return statement(step)

@ask.intent('dishsearchbyingredients',mapping={'ing':'ingredient'})
def dish_search_by_ing(ing):
    print 'Inside side serach by ing'
    with open('ingList.txt','a') as fp:
        fp.write(ing)
    return question('Would you like to add another ingredient or should i search for dish ?')

@ask.intent('addingredient',mapping={'ing':'ingredient'})
def add_ingredient(ing):
    print 'Inside add ingredient by ing'
    with open('ingList.txt','a') as fp:
        fp.write('\n'+ing)
    return question('Would you like to add another ingredient or should i search for dish ?')
@ask.intent('ingdishsearchfromfile')
def ing_dish_search_from_file():
    print 'Ingredient dish search final'
    l=ing_dish_from.searchdishfroming()
    print l
    return question(" Searched successfully, would you like to hear results ?")

@ask.intent('categorydishsearch',mapping={'category':'Category','cuisine':'Cuisine'})
def category_dish_search(category,cuisine):
    print 'inside category search'
    text=getcategorydish(category,cuisine)
    print text
    return statement(text)
@ask.intent('getdishingredients',mapping={'dishname':'DishName'})
def get_dish_ing(dishname):
    ing = ingFunc.getIngList(dishname)
    return statement('...'.join(ing))

def saveHtml(soup,html):
    html.close()
    html = soup.prettify("utf-8")
    with open("./web/index.html", "wb") as file:
        file.write(soup.prettify(formatter=None))
    
def editHtmlFile(dishname='Brocolli'):
    FILENAME='./web/index.html'
    data=open(FILENAME)
    soup=BeautifulSoup(data,"html.parser")
    with open('recipesteps.txt','r') as fp:
        steps=fp.readlines()
    with open('recipeingridients.txt','r') as fp:
        ings=fp.readlines()
    with open('imgurl.txt','r') as fp:
        imgurl=fp.readlines()
    item=soup.find('h2',attrs={'id':'dishname'})
    item.contents[0].replaceWith(dishname)
    item=soup.find('img',attrs={'id':'recimg'})
    item['src']=imgurl
    text='<ul class="list-group">'
    for step in steps:
        text+='<li class="list-group-item"><h4>'+step+'</h4></li>'
    text+='</ul>'
    item=soup.find('div',attrs={'id':'steps'})
    item.clear()
    item.append(text)
    print item
    saveHtml(soup,data)

if __name__ == '__main__':
    app.run(debug=True)