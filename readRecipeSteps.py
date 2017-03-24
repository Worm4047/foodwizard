def readNext(fileName):
	i=''
	n=''
	count=0
	for line in open('index.txt'):
		if count==0:
			i=int(line)
		else:
			n=int(line)
		count+=1

	if i>=n:
		return 'Reached end of search results'	
	i=int(i)+1
	contents=[]
	for line in open(fileName):
		contents.append(line)
	with open('index.txt','w') as m:
		m.write(str(i))
		m.write('\n')
		m.write(str(n))
	return contents[i]
          
def readPrev(fileName):
	i=''
	n=''
	count=0
	for line in open('index.txt'):
		if count==0:
			i=int(line)
		else:
			n=int(line)
		count+=1
	i-=1
	if i<0:
		return 'Reached beginning of search results'
	contents=[]
	for line in open(fileName):
		contents.append(line)
	with open('index.txt','w') as m:
		m.write(str(i))
		m.write('\n')
		m.write(str(n))
	return contents[i]


def readNthLine(fileName,ind):
	i=''
	n=''
	count=0
	for line in open('index.txt'):
		if count==0:
			i=int(line)
		else:
			n=int(line)
		count+=1
	if ind>=n:
		return 'Reached end of search results'
	contents=[]
	for line in open(fileName):
		contents.append(line)
	return contents[ind]










