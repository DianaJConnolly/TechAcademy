#Diana Connolly
#Python 

#Item 36 Drill 
#Requirements from the drill are listed by number ahead of the code that satisfies that requirement.
#This program doesn't really do anything expect illustrate the requirements

import module36

# 1, 8, 9, use of +=, ==, =
#Three functions that compute the sum of the numbers in a given 
#list using a for-loop, a while-loop, and recursion; return the sum from each.

#define input parameter:
numList = [23, 34, 45, 56, 67, 78, 89, 90, 98, 87, 76, 65]
print "original list :" ,
print numList
#call the function and print returned value:
mySum = module36.sumFor(numList)
print "sum of original list using for loop",
print mySum
#call the function and print returned value:
mySum = module36.sumWhile(numList)
print "sum of original array using while loop",
print mySum
#Let's define a list that has a list in it
numList = [23, 34, 45, [56, 67, 78, 89], 90, 98, 87, 76, 65]
#call the function and print returned value:
mySum = module36.sumRec(numList)
print "sum of list that contains a list using a recursive for loop",
print mySum
print

# use of not
#practice enumerate and append functionality
#Write a function that combines two lists by alternatingly taking elements. 
#For example: given the two lists [a, b, c] and [1, 2, 3], the function 
#should return [a, 1, b, 2, c, 3].

numList = [23, 34, 45, 56, 67, 78, 89, 90, 98]
strl = ["this", "that", "other", "hat", "porcupine", "pie", "in", "your", "eye"]
print "original list of numbers: ",
print numList
print "original list of strings: ",
print strl
newl = module36.alternate(numList, strl)  
print "output of alternate function: ",
print newl
print

# 2, 12, 13, use of +
#Write a function that given a list of non negative integers, each no longer than 3 digits,
#arranges them such that they form the largest possible number. 
#For example, given [50, 2, 1, 9], the largest formed number is 95021.
#return final value as string

numList = [788, 50, 2, 1, 9, 43, 203, 267] 
numTuple = tuple(numList)

print "original list: ",
print numList
largest_possible_value = module36.findLargest(numList)
print "largest possible value that can be constructed with original list contents: "
print largest_possible_value
print

# 10, 11, use of *
#Create a tuple from a list and print using for loop

numList = [788, 50, 2, 1, 9, 43, 203, 267] 
print "original list: ",
print numList
print "now printing each list item on a separate line: "
for n in numList:
	print n
#now change numList so tuple has different values
for i, n in enumerate(numList, start=0):
	numList[i] = n * 2
numTuple = tuple(numList) 
print "original tuple :"
print numTuple
print "now printing each tuple item on a separate line: "
for n in numTuple:
	print n
print

# 3, 4, 7 use of and
#Use of .format() notation to truncate strings of different length and format numeric output
str1 = "supercalifragalisticexpialidociousyoucantastethesoundofitnomatterwhereyougopickle"
str2 = "smallshare"
str3 = "biggertoesonnightstiptoetothe"
str4 = "tiny"
str5 = ""
print "original string: "
print str1
print "after truncation: "
print module36.strTruncate(str1)
print "original string: "
print str2
print "after truncation: "
print module36.strTruncate(str2)
print "original string: "
print str3
print "after truncation: "
print module36.strTruncate(str3)
print "original string: "
print str4
print "after truncation: "
print module36.strTruncate(str4)
print "original string: "
print str5
print "after truncation: "
print module36.strTruncate(str5)
numFloat = 4.5567788889
print "formatting " + str(numFloat) + " to 3 significant digits"
print '{0:.3f}'.format(numFloat)
print

# use of /, %
#print whether a number in a list is even or odd
#divide by float or int 
#numList = [788, 50, 2, 1, 9, 43, 203, 267] 
numList = [9, 6, 21, 11] 
m = 0
x = 0.0
s = 0.0
for n in numList:
	print n, 
	if n%2 == 0:
		print " is even"
	else:
		print " is odd"
print
for n in numList:
	print n, 
	print "divided by 3 = ",
	m = n/3
	print m
	print n, 
	print "divided by 3.0 = ",
	x = float(n)/3
	print x
	print n, 
	print "divided by 3 using subtraction = : ",
	s = n
	count = 0
	while(s >= 3):
		s -= 3
		count += 1
	print count,
	print " remainder ", 
	print s

	








