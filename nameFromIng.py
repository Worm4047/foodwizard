try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

import requests
import json  

def findDishes(soup):
	app=[]
	for item in soup.find_all('h3',attrs={'class':'grid-col__h3 grid-col__h3--recipe-grid'}):
		title=item.text
		title=title.replace('\n','')
		title=title.replace('\r','')
		title=title.strip()
		if not title in app:
			app.append(title)
	return app

if __name__=="__main__":
	baseUrl='http://allrecipes.com/search/results'
	res=[]
	for page in range(1,5):
		params = dict(
		    ingIncl='bread,butter',
		    sort='re',
		    page=page
		)
		resp = requests.get(url=baseUrl, params=params)
		data = resp.text	
		soup = BeautifulSoup(data,"html.parser")
		# print soup
		dishes = findDishes(soup)
		res=res+dishes
		print len(dishes)
	print len(res)
	# l=min(data['count'],5)
	# for r in data['recipes']:
	# 	if l==0:
	# 		break
	# 	l-=1
	# 	title=r['title']
	# 	if '(' in title:
	# 		ind=title.index('(')
	# 		title=title[:ind]
	# 	print title

	
	


