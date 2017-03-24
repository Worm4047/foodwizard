try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

def saveHtml(soup,html):
	html.close()
	html = soup.prettify("utf-8")
	with open("./web/index.html", "wb") as file:
		file.write(soup.prettify())
	data = open('./web/index.html','wb')
	data=data.replace('&lt;','<')
	data=data.replace('&gt;','>')
	with open("./web/index.html", "wb") as file:
		file.write(data)

def editHtmlFile():
    FILENAME='./web/index.html'
    data=open(FILENAME)
    soup=BeautifulSoup(data,"html.parser")
    with open('recipesteps.txt','r') as fp:
        steps=fp.readlines()
    with open('recipeingridients.txt','r') as fp:
        ings=fp.readlines()
    with open('imgurl.txt','r') as fp:
        imgurl=fp.readlines()
   

    text='<ul>'
    for step in steps:
        text+='<li>'+step+'</li>'
    text+='</ul>'
    item=soup.find('div',attrs={'id':'steps'})
    item.clear()
    item.append(text)
    print item
    saveHtml(soup,data)

editHtmlFile()