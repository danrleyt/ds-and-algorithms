
def reverseRecursive(s):
	if len(s) == 1:
		return s
	return reverseRecursive(s[1:]) + s[0]

s = 'abcde'
print(reverseRecursive(s))

def count_x(s):
	if len(s) == 0:
		return 0
	if s[0] == 'x':
		return 1 + count_x(s[1:])
	else:
		return count_x(s[1:])

s = 'axbxcxdx'
print(count_x(s))

def n_paths(steps):
	if steps < 0: 
		return 0 
	if steps == 1 or steps == 0:
		return 1
	return n_paths(steps - 1) + n_paths(steps - 2) + n_paths(steps - 3)

n = 11
print(n_paths(n))

def anagram_of(string):
	if len(string) == 1:
		return [string[0]]
	collection = []

	substring_anagrams = anagram_of(string[1:])

	for sub in substring_anagrams:
		for index in range(0, len(sub)+1):
			collection.append(sub[:index] + string[0] + sub[index:])
	
	return collection 

print(anagram_of('abc'))


# Question 1
def countChars(arr):
	if len(arr) == 0:
		return 0
	return len(arr[0]) + countChars(arr[1:])
ar = ['ab', 'c', 'def', 'ghij']
print('Q1: ' + str(countChars(ar)))

# Question 2
def returnEven(arr):
	if len(arr) == 0:
		return []
	if arr[0] % 2 == 0:
		return [arr[0]] + returnEven(arr[1:])
	else:
		return returnEven(arr[1:])

ar = [1,2,3,4,5,6]
print('Q2: '+ str(returnEven(ar)))

# Question 3
def triangularNumber(n):
	if n <= 0:
		return 0
	if n == 1:
		return 1
	return n + triangularNumber(n-1)

print('Q3: ' + str(triangularNumber(8)))


# Question 4
def index_of_x(s):
	if s[0] == 'x':
		return 0
	return index_of_x(s[1:]) + 1

s = 'abcdex'
print('Q4: ' + str(index_of_x(s)))

# Question 5
def shortest_path(r, c):
	if r == 1 or c == 1:
		return 1 
	return shortest_path(r - 1, c) + shortest_path(r, c - 1)

print('Q5: '+ str(shortest_path(3, 7)))
