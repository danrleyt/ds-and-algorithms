def bubbleSort(arr):
	size = len(arr)
	sorted = False
	while not sorted:
		sorted = True
		for i in range(size-1):
			if arr[i] > arr[i+1]:
				sorted = False
				temp = arr[i]
				arr[i] = arr[i+1]
				arr[i+1] = temp
	return arr

arr_test = [5,4,3,2,1]

c = bubbleSort(arr_test)

print (c)