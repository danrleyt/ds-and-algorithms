def selectionSort(arr):
	size = len(arr)
	for i in range(0, size):
		lowest = i
		for j in range(i+1, size):
			if arr[j] < arr[lowest]:
				lowest = j
		if lowest != i:
			temp = arr[i]
			arr[i] = arr[lowest]
			arr[lowest] = temp		
	return arr
		


arr_test = [5,4,3,2,1]

print (selectionSort(arr_test))