try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

import requests  

BASEURL = 'http://allrecipes.com'
LIMIT = 5
DATAFILE = 'dishsearchresult.txt'

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
		items.append((htag.text.strip()).lower()+'::::'+BASEURL+item['href'])
		if i >= LIMIT*2:
			break;
	return '\n'.join(items),len(items)

def getDishesByName(query):
	baseUrl='http://allrecipes.com'	
	#q='bread and butter pudding'
	url = "http://allrecipes.com/search/results/?wt="+query+"&sort=re"
	#http://allrecipes.com/search/results/?wt=bread and butter pudding&sort=re
	r  = requests.get(url)
	data = r.text

	soup = BeautifulSoup(data,"html.parser")
	res,n = findArticles(soup)

	with open(DATAFILE,'w') as resultfile:
		resultfile.write(res)
	return n


