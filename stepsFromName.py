try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

import requests  

def findArticle(soup)
	for item in soup.find_all('a',attrs={'data-internal-referrer-link':'hub recipe'}):
		return item['href']

def getSteps(soup):
	steps=[]
	for item in soup.find_all('ol',attrs={'class':'list-numbers recipe-directions__list'}):
		for step in item.find_all('li'):
			steps.append(step.text)
	return steps


if __name__=="__main__":
	baseUrl='http://allrecipes.com'	
	q='bread and butter pudding'
	url = "http://allrecipes.com/search/results/?wt="+q+"&sort=re"
	r  = requests.get(url)
	data = r.text
	# print data
	soup = BeautifulSoup(data,"html.parser")
	#Todo - 5 dishes names::::url 
	##Save them into a text file
	##Return number of result

	#obsolete
	# urlStepsPage = findArticle(soup)
	# r  = requests.get(baseUrl+urlStepsPage)
	# data = r.text
	# # print data
	# soup = BeautifulSoup(data,"html.parser")
	# steps = getSteps(soup)
	# print steps
	
	


