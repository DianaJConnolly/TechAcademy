
#function to sum list values using for loop:
def sumFor(numl):
	sumf = 0
	for n in numl:
		sumf += n
	return sumf;

#function to sum list values using for while loop:
def sumWhile(numl):
	sumw = 0
	count = 0
	while count < len(numl):
		sumw += numl[count]
		count += 1
	return sumw;

#recursive function to add elements of list:
def sumRec(numl):
	sumR = 0
	for n in numl:
	    if type(n) == type([]): #if the element is a list
	        sumR += sumRec(n) 	#call the function recursively to add the internal list elements
	    else:
	        sumR += n   		#else just add the next element
	return sumR;

#alternately combine two lists and return alternated list.	
def alternate(lst1, lst2):
	altl = []
	if not(len(lst1) == len(lst2)):
		print "error! lists must be of same size, exiting...."
		return -1
	#need enumerate to get index so we can access different lists
	for index, item in enumerate(lst1, start=0):
		altl.append(lst1[index])
		altl.append(lst2[index])
	return altl

## create a custom comparator for findLargest() function
def comparator(x, y):
	rtn = 0
	str1 = str(x) + str(y)
	str2 = str(y) + str(x)
	if str1 < str2:
		rtn = 1
	if str1 > str2:
		rtn = -1
	return rtn
def findLargest(numList):
	numList.sort(comparator)
	#convert to string to concatenate
	numString = ""
	for n in numList:
		numString += str(n)
	#convert back to integer value
	return numString

#use .format to do truncate strings of different lengths based on size parameters
def strTruncate(str):
	#print str
	strTemp = ""
	l = len(str)
	if l == 0:
		strTemp = "your string is empty"
	if l != 0 and l <= 10:
		strTemp = '{:.5}'.format(str)
	elif l > 10 and l <= 30:
		strTemp = '{:.10}'.format(str)
	else:
		strTemp =  "your string is just too big to process"
	return strTemp
