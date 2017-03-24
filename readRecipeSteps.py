
def readNext(fileName):
	i=''
	for line in open('index.txt'):
		i=int(line)
	i+=1
	contents=[]
	for line in fileName:
		contents.append(line)
	with open('index.txt','w') as m:
		m.write(i)
	return contents[i]
          
def readPrev(fileName):
	i=''
	for line in open('index.txt'):
		i=int(line)
	i-=1
	contents=[]
	for line in fileName:
		contents.append(line)
	with open('index.txt','w') as m:
		m.write(i)
	return contents[i]


def readNthLine(fileName,n):
	contents=[]
	for line in fileName:
		contents.append(line)
	return contents[n]










