from audioop import reverse
from tokenize import Number


class Stack:
    def __init__(self) -> None:
        self.elements = []

    def size(self):
        return len(self.elements)

    def push(self, element):
        self.elements.append(element)

    def read(self):
        if self.size() > 0:
            return self.elements[self.size()-1]
        return None

    def pop(self):
        if self.size() > 0:
            return self.elements.pop()
        return None


def reverseStr(s):
    rStack = Stack()
    for char in s:
        rStack.push(char)

    res = ''
    while rStack.read() != None:
        res += rStack.pop()
    return res

s = 'abcde'
print (reverseStr(s))
