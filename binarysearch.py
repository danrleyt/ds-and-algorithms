from sqlalchemy import null


def binarySearch(arr, value):
	lower_bound = 0
	upper_bound = len(arr) - 1

	while lower_bound <= upper_bound:
		middlepoint = (lower_bound + upper_bound) // 2
		value_at_middle = arr[middlepoint]

		if value_at_middle == value:
			return middlepoint
		elif value > value_at_middle :
			lower_bound = middlepoint + 1
		elif value < value_at_middle:
			upper_bound = middlepoint - 1
		
	return null




arr_test = [1,2,3,4,5]
print (binarySearch(arr_test, 5))