# Question 3
def sum(low, high):
	print(low, high)
	if high == low:
		return low
	return high + sum(low, high - 1)

print (sum(1,10))
print("--------------x--------------")

# Question 4

def printNumbers(arr):
	for el in arr:
		if type(el) is int:
			print(el)
		else:
			printNumbers(el)


array = [
	1,
	2,
	3,
	[4,5,6],
	7,
	[8, 
		[9, 10,11,
			[12,13,14]
		]
	],
	[15,16,17,18,19,
		[20,21,22,
			[23,24,25,
				[26,27,29,28]
			], 30, 31
		], 32
	],33
]

printNumbers(array)

# Question extra Fibonacci

def printFibAtN(n):
	if n <=1:
		return n
	return printFibAtN(n-1) + printFibAtN(n-2)

print(printFibAtN(4))