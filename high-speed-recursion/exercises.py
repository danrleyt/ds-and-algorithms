# Question 1
def multipleOfMax3(arr):
	s = sorted(arr)
	if len(s) >= 3:
		return s[len(s)-3] * s[len(s)-2] * s[len(s)-1]
	return None

# Question 2 
def findMissingNumber(arr):
	so = sorted(arr)
	for i in range(0, len(so)):
		if i != so[i]:
			return i
	return None

# Question 3
def findON2(arr):
	maxN = arr[0]
	for i in range(0, len(arr)):
		for j in range(1, len(arr)):
			if arr[j] > arr[i]:
				maxN = arr[j]
	return maxN

def findON(arr):
	maxN = arr[0]
	for i in range(1, len(arr)):
		if arr[i] > maxN:
			maxN = arr[i]
	return maxN

def findONlogN(arr):
	so = sorted(arr)
	return so[len(so) - 1]

ar = [1,2,3,4,5,6]
print (findON2(ar))
print (findON(ar))
print (findONlogN(ar))