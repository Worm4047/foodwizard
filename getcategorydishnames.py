
LIMIT=10

""" 
	searches for dishes matching the required category and cuisine 
	args : query name of category and cuisine
	returns : list of 10 dishes
"""
def getcategorydish(category,cuisine):
	folder=category
	category=list(category)
	category[0]=category[0].upper()
	category=''.join(category)
	filename='textdata/'+cuisine+'/'+cuisine+category+'.txt'
	items=[]
	for line in open(filename):
		if not line in items:
			items.append(line)
	return '...'.join(items[:min(len(items),LIMIT)])


#print getcategorydish('Appetizers','indian')