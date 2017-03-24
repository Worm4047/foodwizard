
def readNext(fileName,index):
	with open(fileName) as fp:
		for i, line in enumerate(fp):
			if i == index:
				return line

		return "No next line"		
	fp.close()



            
def readPrev(fileName,index):
	prev=""
	with open(fileName) as fp:
		for i, line in enumerate(fp):
			if i+1 == index:
				if not prev:
					break

				return prev
			prev=line

		return "No prev Line"		
	fp.close()


def readNthLine(fileName,index):
	with open(fileName) as fp:
		for i, line in enumerate(fp):
			if i+1 == index:
				return line

		return "No such Line"

	fp.close()




if __name__=="__main__":
	result=readNthLine("results.txt",2)

	print result

	result=readPrev("results.txt",2)

	print result









