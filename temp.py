try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

def saveHtml(soup,html):
	html.close()
	html = soup.prettify("utf-8")
	with open("./web/index.html", "wb") as file:
		file.write(soup.prettify(formatter=None))
	
def editHtmlFile(dishname='Brocolli'):
    FILENAME='./web/index.html'
    data=open(FILENAME)
    soup=BeautifulSoup(data,"html.parser")
    with open('recipesteps.txt','r') as fp:
        steps=fp.readlines()
    with open('recipeingridients.txt','r') as fp:
        ings=fp.readlines()
    with open('imgurl.txt','r') as fp:
        imgurl=fp.readlines()
	item=soup.find('h2',attrs={'id':'dishname'})
    item.contents[0].replaceWith(dishname)
    item=soup.find('img',attrs={'id':'recimg'})
    item['src']=imgurl
    text='<ul class="list-group">'
    for step in steps:
        text+='<li class="list-group-item"><h4>'+step+'</h4></li>'
    text+='</ul>'
    item=soup.find('div',attrs={'id':'steps'})
    item.clear()
    item.append(text)
    print item
    saveHtml(soup,data)

editHtmlFile()