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
	return '...'.join(items[:10])
