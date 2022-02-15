def insertionSort(arr):
	for index in range(1, len(arr)):
		temp_value = arr[index]
		position = index - 1 
		while position >= 0:
			if arr[position] > temp_value:
				arr[position+1] = arr[position]
				position = position - 1
			else: 
				break
		arr[position + 1] = temp_value
	return arr


arr_test = [5,4,3,2,1]
print (insertionSort(arr_test))