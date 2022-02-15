class Node:
	next_node = None
	def __init__(self, data):
		self.data = data
		self.next_node = None
	
class LinkedList:
	head = None
	def __init__(self, node) -> None:
		self.head = node
	def readAt(self, index):
		current_node = self.head
		current_index = 0
		while current_index < index:
			current_node = current_node.next_node
			current_index += 1 
			if current_node == None:
				return None
		return current_node.data
	def indexOf(self, value):
		current_node = self.head
		current_index = 0
		while current_node != None:
			if current_node.data == value:
				return current_index
			current_node = current_node.next_node
			current_index += 1
		return None
	def insertAt(self, index, value):
		newNode = Node(value)
		if index == 0:
			newNode.next_node = self.head
			self.head = newNode
			return
		
		current_node = self.head
		current_index = 0

		while current_index < (index - 1):
			current_node = current_node.next_node
			current_index += 1
		newNode.next_node = current_node.next_node
		current_node.next_node = newNode
	def deleteAt(self, index):
		if index == 0:
			self.head = self.head.next_node
			return
		
		current_node = self.head
		current_index = 0

		while current_index < (index - 1):
			current_node = current_node.next_node
			current_index += 1
		
		node_after = current_node.next_node.next_node
		current_node.next_node = node_after
	# Question 1
	def printAll(self):
		if not self.head:
			print(None)
			return
		else:
			current_node = self.head
			while current_node:
				print(current_node.data)
				current_node = current_node.next_node
	# Question 3
	def getLast(self):
		if not self.head:
			return None
		else:
			current_node = self.head
			while current_node.next_node:
				current_node = current_node.next_node
			return current_node.data
	# Question 4
	def reverseList(self):
		previous_node = None
		current_node = self.head

		while current_node:
			next_node = current_node.next_node

			current_node.next_node = previous_node
			previous_node = current_node

			current_node = next_node	

l = LinkedList(Node('a'))
print(l.readAt(0))
print(l.indexOf('a'))
l.insertAt(1, 'b')
l.insertAt(2, 'c')
print(l.readAt(1))
print(l.readAt(2))
print(l.readAt(1))
l.printAll()
print(l.getLast())

