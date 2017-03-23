try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

import requests  

def findArticle(soup)
	for item in soup.find_all('a',attrs={'data-internal-referrer-link':'hub recipe'}):
		return item['href']
		
def getSteps(q):
	baseUrl='http://allrecipes.com'	
	url = "http://allrecipes.com/search/results/?wt="+q+"&sort=re"
	r  = requests.get(url)
	data = r.text
	soup = BeautifulSoup(data,"html.parser")
	steps = getSteps(soup)
	steps=[]
	for item in soup.find_all('ol',attrs={'class':'list-numbers recipe-directions__list'}):
		for step in item.find_all('li'):
			steps.append(step.text)
	return steps

	


