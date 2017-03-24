try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

import requests  


""" 
	reads the searchresult file for names and urls of dishes
	args : query name of dish
	returns : url of the dish recipe
"""

def geturlFromFile(query):
	print query
	filename='dishsearchresult.txt'
	dish={}
	for line in open(filename):
		name,url=line.split('::::')
		dish[name]=url
	return dish[query]


""" 
	searches for recipe of a dish and writes the steps to a file
	args : query name of dish
	returns : number of  steps in recipe
"""

def getSteps(dishname):
	url=geturlFromFile(dishname.lower()).replace('\n','')
	print url
	# url = "http://allrecipes.com/recipe/212392/loukoumades/?internalSource=hub%20recipe&referringContentType=search%20results&clickId=cardslot%201"
	r  = requests.get(url)
	data = r.text
	soup = BeautifulSoup(data,"html.parser")
	steps=[]
	for item in soup.find_all('ol',attrs={'class':'list-numbers recipe-directions__list'}):
		for step in item.find_all('li'):
			steps.append(step.text)
	print steps
	item = soup.find('img',attrs={'class':'rec-photo'})
	imgurl=item['src']
	with open('imgurl.txt','w') as myfile:
		myfile.write(imgurl)
	with open('recipeSteps.txt','w') as myfile:
		myfile.write('\n'.join(steps))
	with open('index.txt','w') as myfile3:
		myfile3.write('-1')
		myfile3.write('\n')
		myfile3.write(str(len(steps)))
	return len(steps)

	


