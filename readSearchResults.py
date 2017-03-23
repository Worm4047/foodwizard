
def returnResults(fileName):
	result=""
	for line in open(fileName):
		(name,url)=line.split('::::')
		result=result+name+'\n'

	return result		
