range_1 = 10
range_2 = 10

"""
1. Write a program that reads two lists
	 of numbers (4 items minimum) and merge
   them by sorting them out ignoring duplicates
"""
list1 = [1 * i for i in range(range_1)] # n * 1
list2 = [2 * i for i in range(range_2)] # n * 2
#list2 = list2[::-1] # reverse the list order

def mergeNonDuplicates(list1, list2):
		return sorted(list(set(list1+list2)))

print("1: ",mergeNonDuplicates(list1, list2))

"""
2. Improve the previous code by ignoring the ones
	 that could be written as a linear combination of
	 any other two numbers (13 = 2*x + 1*y), so if 3 and
	 5 are there, you should drop 13 if seen.

	 [v1v2]x = b
"""
def exists(element, collection: iter):
    return element in collection

def improveMerge():
	merged = mergeNonDuplicates(list1,list2) 
	for i in merged:
		a = (1 * i)
		for ii in merged:
			b = a + (2 * ii)
			if exists(b,merged):
					merged.remove(b)

	return merged


print("2: ",improveMerge()) 