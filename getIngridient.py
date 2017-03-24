try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

import requests  

BASEURL = 'http://allrecipes.com'
LIMIT = 5
DATAFILE = 'recipeingridients.txt'
BASE_FILE = 'dishsearchresult.txt'
def findIngridients(soup):
	i = 0
	items = []
	for item in soup.find_all('span',attrs={'class':'recipe-ingred_txt added'}):
	#for item in ar.find_all('a',attrs={'data-internal-referrer-link':'hub recipe'}):
		var = item.text.strip()
		#print var
		if var != 'None':
			items.append(var)
	return '\n'.join(items),len(items)

def getIngList(name):
	dish = {}
	for line in open(BASE_FILE):
		dname,durl = line.split('::::')
		dish[dname]=durl
	#print dish['Egg Curry']
	#print url
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
	return n
	
#print getIngList('Curried Coconut Egg Drop Soup')

