"""http://stackoverflow.com/questions/24825366/python-how-to-cut-a-list-which-contains-lists/24827627#24827627
"""
list1 = [ [1,2,3,4],     [5,6,7,8],     [9,10,11,12] ]
list2 = [ [50,45,40,35], [30,25,20,15], [10,9,5,0]   ]
list3 = [ [101,2,3,33],  [11,22,30,1],  [1,22,33,]   ]

def func_index(reference, number):
	index = 0
	for ind1, value1 in enumerate(reference):
		for ind2, value2 in enumerate(value1):
			index += 1
			if value2 == number:
				return index

def func_slice(lst, index):
	count = 0
	temp = []
	for ind1, value1 in enumerate(lst):
		for ind2, value2 in enumerate(value1):
			count += 1
			if count == index:
				temp.append(value1[:ind2+1])
				return temp
		temp.append(value1)			
	return temp					
list2 = func_slice(list2, func_index(list1, 9))
list3 = func_slice(list3, func_index(list1, 2))
print list2
print list3
