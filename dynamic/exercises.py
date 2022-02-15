# Question 1
def add_until_100(arr):
    if len(arr) == 0:
        return 0
    remainder = add_until_100(arr[1:])
    if arr[0] + remainder > 100:
        return remainder
    else:
        return arr[0] + remainder


ar = [1, 2, 3, 4, 5, 6, 7]
print(add_until_100(ar))

# Question 2
def golomb(n, memo={}):
    if n == 1:
        return 1
    if not memo.get(n):
        memo[n] = 1 + golomb(n - golomb(golomb(n-1, memo), memo), memo)
    return memo[n]

# Question 3
def unique_paths(rows, columns, memo={}):
    if rows == 1 or columns == 1:
        return 1
    if not memo.get((rows, columns)):
        memo[(rows, columns)] = unique_paths(
            rows-1, columns, memo) + unique_paths(rows, columns-1, memo)
    return memo[(rows, columns)]


print(unique_paths(3, 7))
