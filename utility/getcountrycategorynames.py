try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

import requests  

def findArticle(soup):
	for item in soup.find_all('a',attrs={'data-internal-referrer-link':'hub recipe'}):
		return item['href']

def findDishes(soup):
	app=[]
	for item in soup.find_all('h3',attrs={'class':'grid-col__h3 grid-col__h3--recipe-grid'}):
		title=item.text
		title=title.replace('\n','')
		title=title.replace('\r','')
		title=title.strip()
		if '(' in title:
			ind=title.index('(')
			title=title[:ind]
		if not title in app:
			app.append(title)
	return app

if __name__=="__main__":
	names=['indian','chinese','french','greek','italian']
	for inpFile in names:
		n=inpFile
		inpFile+='Url.txt'
		for line in open(inpFile):
			# print line
			saveFileName,baseUrl = line.split('$')
			print saveFileName,baseUrl
			saveFileName=saveFileName.strip()
			saveFileName=n+'/'+saveFileName+'.txt'
			# baseUrl='http://allrecipes.com/recipes/1874/world-cuisine/asian/indian/appetizers/?internalSource=hub%20nav&referringId=233&referringContentType=recipe%20hub&linkName=hub%20nav%20daughter&clickId=hub%20nav%202&page='	
			total=[]
			for i in range(1,5):
				url=baseUrl+str(i)
				print url
				r  = requests.get(url)
				data = r.text
				# print data
				soup = BeautifulSoup(data,"html.parser")
				title = findDishes(soup)
				if len(title) == 0:
					break
				total.append(title)
			with open(saveFileName,'a') as myfile:
				for item in total:
					line='\n'.join(item).encode('utf-8').strip()
					myfile.write('\n'+line)

	
	


