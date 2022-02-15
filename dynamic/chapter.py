def custom_max(arr):
    if len(arr) == 1:
        return arr[0]
    if arr[0] > custom_max(arr[1:]):
        return arr[0]
    else:
        return custom_max(arr[1:])

def custom_max_memo(arr):
	if len(arr) == 1:
		return arr[0]
	max_calculations = custom_max_memo(arr[1:])
	if arr[0] > max_calculations:
		return arr[0]
	else:
		return max_calculations

arr = [1, 2, 3, 4, 5, 6, 7]
print(custom_max(arr))
print(custom_max_memo(arr))


print('*************x*************')

# Fibonacci
def fib(n):
	if n == 0 or n == 1:
		return n
	return fib(n-2) + fib(n-1)

def fib_memo(n, memo={}):
	if n ==0 or n ==1:
		return n
	if not memo.get(n):
		memo[n] = fib_memo(n-2, memo) + fib_memo(n-1, memo)
	return memo[n]

print(fib_memo(10))
print(fib(6))