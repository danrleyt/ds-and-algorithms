# Question 1
def intersection(arr, arr2):
    dic1 = {}
    for val in arr:
        dic1[val] = True
    inter = []
    for val in arr2:
        if dic1.get(val):
            inter.append(val)
    return inter


arr = [1, 2, 3, 4, 5]
arr2 = [0, 2, 4, 6, 8]
print(intersection(arr, arr2))

# Question 2


def findFirstDuplicate(arr):
    dic = {}
    for char in arr:
        if dic.get(char):
            return char
        else:
            dic[char] = True
    return None


arr = ['a', 'b', 'c', 'd', 'c', 'e', 'd', 'f']

print(findFirstDuplicate(arr))

# Question 3


def findMissing(s):
    dic = {}
    for char in s:
        dic[char] = 1
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for a in alphabet:
        if dic.get(a) == None:
            return a
    return False


s = "the quick brown box jumps over a lazy dog"
print(findMissing(s))

# Question 4


def firstUnique(s):
    dic = {}
    for char in s:
        if dic.get(char) != None:
            dic[char] += 1
        else:
            dic[char] = 1
    for char in s:
        if dic.get(char) == 1:
            return char


s = "minimum"
print(firstUnique(s))
