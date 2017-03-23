def readNext(fileName):
	r=''
	for line in open('index.txt'):
		r=line
	i=int(r)+1
	with open(fileName) as fp:
		content=fp.readlines()
	with open('index.txt','w') as myfile:
		myfile.write(str(i))
	return content[i]		
            
def readPrev(fileName):
	r=''
	for line in open('index.txt'):
		r=line
	i=int(r)-1
	with open(fileName) as fp:
		content=fp.readlines()
	with open('index.txt','w') as myfile:
		myfile.write(str(i))
	return content[i]	


def readNthLine(fileName,n):
	with open(fileName) as fp:
		content=fp.readlines()
	return content[n]	




if __name__=="__main__":
	result=readNthLine("results.txt",2)

	print result

	result=readPrev("results.txt",2)

	print result









