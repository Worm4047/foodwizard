with open('textdata/alldishesname.txt','r+') as f:
	content = f.readlines()
	# you may also want to remove whitespace characters like `\n` at the end of each line
	content = list(set([x.strip() for x in content]))
	for item in content:
		print item
	# f.write('\n'.join(content))
