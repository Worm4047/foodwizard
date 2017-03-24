try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

import requests  


BASEURL = 'http://allrecipes.com'
LIMIT = 5
DATAFILE = 'recipeingridients.txt'
BASE_FILE = 'dishsearchresult.txt'



""" 
	parshes html content to get indridients 
	args : BeautifulSoup object 
	returns : list of ingridients
"""

def findIngridients(soup):
	i = 0
	items = []
	for item in soup.find_all('span',attrs={'class':'recipe-ingred_txt added'}):
	#for item in ar.find_all('a',attrs={'data-internal-referrer-link':'hub recipe'}):
		var = item.text.strip()
		#print var
		if var != 'None':
			items.append(var)
	return '...'.join(items),len(items)


""" 
	searches for ingridients of a particular dish and writes them to a file
	args : query name of dish
	returns : number of ingridients found
"""

def getIngList(name):
	dish = {}
	name=name.lower()
	for line in open(BASE_FILE):
		dname,durl = line.split('::::')
		dish[dname]=durl
	url = dish[name].strip()
	r  = requests.get(url)
	data = r.text
	# print data
	soup = BeautifulSoup(data,"html.parser")
	#print soup

	# get ingidient string and number
	res,n = findIngridients(soup)
	with open(DATAFILE,'w') as resultfile:
		resultfile.write(res)
	return res
	
#print getIngList('Curried Coconut Egg Drop Soup')

