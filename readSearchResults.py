
def returnResults(fileName):
	result=[]
	for line in open(fileName):
		(name,url)=line.split('::::')
		result.append(name)
	return '...'.join(result)		
