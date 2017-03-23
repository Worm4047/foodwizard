try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

import requests  

# def findArticle(soup):
# 	for item in soup.find_all('a',attrs={'data-internal-referrer-link':'hub recipe'}):
# 		return item['href']

def getSteps(dishname):
	url = "http://allrecipes.com/recipe/212392/loukoumades/?internalSource=hub%20recipe&referringContentType=search%20results&clickId=cardslot%201"
	r  = requests.get(url)
	data = r.text
	soup = BeautifulSoup(data,"html.parser")
	steps=[]
	for item in soup.find_all('ol',attrs={'class':'list-numbers recipe-directions__list'}):
		for step in item.find_all('li'):
			steps.append(step.text)
	with open('recipeSteps.txt','w') as myfile:
		myfile.write('\n'.join(steps))
	return len(steps)

	


