try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

import requests  

def getIngredients(soup):
	ings=[]
	for ing in soup.find_all('ol',attrs={'class':'resources'}):
		for an in ing.find_all('a'):
			# print an.text
			item=(an.text).replace('\n','')
			item=item.strip()
			if 'Related' in item:continue
			ings.append(item)

	return ings

if __name__=="__main__":
	baseUrl='http://www.bbc.co.uk/food/ingredients/by/letter/'
	li='abcdefghijklmnopqrstuvwxyz'
	total=[]
	for x in range(26):
		url=baseUrl+li[x]	
		print url
		r  = requests.get(url)
		data = r.text
		# print data
		soup = BeautifulSoup(data,"html.parser")
		ings = getIngredients(soup)
		# print ings
		total.append(ings)
	with open('ingredients.txt','a') as myfile:
		for li in total:
			line='\n'.join(li).encode('utf-8').strip()
			myfile.write('\n'+line)


	
	


