'''Write your own version of the sorted() method in Python. 
This method should take a list1 as an argument and return a list1 that is 
sorted in ascending order. Call your method passing in the following 
lists as arguments and print out each sorted list1 to the shell. 
This should be an algorithm that you write. Do not use .sort() or the sorted() methods in your method.

[67, 45, 2, 13, 1, 998]
[89, 23, 33, 45, 10, 12, 45, 45, 45]

Your sorted lists should look like this when displayed:
[1, 2, 13, 45, 67, 998]
[10, 12, 23, 33, 45, 45, 45, 45, 89]
'''
list1 = [67, 45, 2, 13, 1, 998]
list2 = [89, 23, 33, 45, 10, 12, 45, 45, 45]

def sort(listX):
	tmp = 0
	for i in range(len(listX)-1):
		for i in range(len(listX)-1):
			if(listX[i] > listX[i+1]):
				#swap
				tmp = listX[i]
				listX[i] = listX[i+1]
				listX[i+1] = tmp
	return listX

print("original list1"),
print(list1)
print("original list2"),
print(list2)

sort(list1)
sort(list2)

print("after sorting list1"),
print(list1)
print("after sorting list2"),
print(list2)

