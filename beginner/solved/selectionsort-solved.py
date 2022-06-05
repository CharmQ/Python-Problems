'''

Selection Sort Problem

Create a code that sorts a list by examining through the list, picking the largest value, and putting it in the end. Repeat until list is sorted.

'''

import random

def sort(n,m):
	myList = [random.randint(0,m) for i in range(n)]
	print(f'List: {myList}')
	sub = 1
	for i in range(len(myList) - 1):
		track = 0
		curr = myList[0]
		for i in range(len(myList) - sub):
			if curr <= myList[i+1]:
				curr = myList[i+1]
				track = i + 1
		myList.insert(len(myList) - sub, myList.pop(track))
		sub = sub + 1
	print(f'Sorted: {myList}')

sort(10,100)