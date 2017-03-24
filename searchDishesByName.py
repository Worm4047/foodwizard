try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

import requests  

BASEURL = 'http://allrecipes.com'
LIMIT = 5
DATAFILE = 'recipesresult.txt'

def findArticles(soup):
	i = 0
	items = []
	for ar in soup.find_all('article'):
	#for item in ar.find_all('a',attrs={'data-internal-referrer-link':'hub recipe'}):
		item = ar.find('a')
		if not item: continue	
		i += 1
		if i%2==0:
			continue
		htag = item.find('h3')
		items.append(htag.text.strip()+'::::'+BASEURL+item['href'])
		if i >= LIMIT*2:
			break;
	return '\n'.join(items),len(items)

# def getSteps(soup):
# 	steps=[]
# 	for item in soup.find_all('ol',attrs={'class':'list-numbers recipe-directions__list'}):
# 		for step in item.find_all('li'):
# 			steps.append(step.text)
# 	return steps


def getDishesByName(query):
	baseUrl='http://allrecipes.com'	
	#q='bread and butter pudding'
	url = "http://allrecipes.com/search/results/?wt="+query+"&sort=re"
	#http://allrecipes.com/search/results/?wt=bread and butter pudding&sort=re
	r  = requests.get(url)
	data = r.text
	# print data
	soup = BeautifulSoup(data,"html.parser")
	#Todo - 5 dishes names::::url 
	##Save them into a text file
	##Return number of result

	#print soup

	res,n = findArticles(soup)

	with open(DATAFILE,'w') as resultfile:
		resultfile.write(res)
	return n
	#print "done"

	#obsolete
	# urlStepsPage = findArticle(soup)
	# r  = requests.get(baseUrl+urlStepsPage)
	# data = r.text
	# # print data
	# soup = BeautifulSoup(data,"html.parser")
	# steps = getSteps(soup)
	# print steps
	
	
print getDishesByName('paneer masala')

