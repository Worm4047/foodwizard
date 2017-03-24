try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

import requests  

BASEURL = 'http://allrecipes.com'
LIMIT = 5
DATAFILE = 'dishsearchresult.txt'



""" 
	parshes html content to get links and names of the dishes
	args : BeautifulSoup object 
	returns : list of dish names and urls
"""
def findArticles(soup):
	items = []
	for ar in soup.find_all('article'):
	#for item in ar.find_all('a',attrs={'data-internal-referrer-link':'hub recipe'}):
		item = ar.find('a')
		if not item: continue	
		for htag in item.find_all('h3',attrs={'class':'grid-col__h3 grid-col__h3--recipe-grid'}):
			if 'recipe' in item['href']:
				temp=item['href'].split('/')
				if len(temp)>3:
					items.append((htag.text.strip()).lower()+'::::'+BASEURL+item['href'])
				
	return '\n'.join(items[0:min(len(items),LIMIT)]),len(items)


""" 
	searches dishes by name and writes to file, name and Url's for recipe
	args : query name of dish
	returns : number of dishes found
"""
def getDishesByName(query):
	url = "http://allrecipes.com/search/results/?wt="+query+"&sort=re"
	print url
	#http://allrecipes.com/search/results/?wt=bread and butter pudding&sort=re
	r  = requests.get(url)
	data = r.text

	soup = BeautifulSoup(data,"html.parser")
	res,n = findArticles(soup)

	with open(DATAFILE,'w') as resultfile:
		resultfile.write(res)
	return n


getDishesByName('egg rolls')