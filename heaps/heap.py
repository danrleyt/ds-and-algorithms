class Heap:
	def __init__(self):
		self.data = []

	def getRoot(self):
		return self.data[0]
	
	def getLast(self):
		return self.data[len(self.data)-1]

	def leftChildIndex(self, index):
		return (index * 2) + 1
	
	def rightChildIndex(self, index):
		return (index * 2) + 2
	
	def parentIndex(self, index):
		return (index - 1) // 2

	def insert(self, value):
		self.data.append(value)

		new_node_index = len(self.data) - 1

		while new_node_index > 0 and self.data[new_node_index] > self.data[self.parentIndex(new_node_index)]:
			self.data[self.parentIndex(new_node_index)], self.data[new_node_index] = self.data[new_node_index], self.data[self.parentIndex(new_node_index)]
			new_node_index = self.parentIndex(new_node_index)

	def hasGreaterChild(self, index):
		return (self.data[self.leftChildIndex(index)] and self.data[self.leftChildIndex(index)] > self.data[index]) or (self.data[self.rightChildIndex] and self.data[self.rightChildIndex(index)] > self.data[index])

	def calculateLargerChild(self, index):
		if not self.data[self.rightChildIndex(index)]:
			return self.leftChildIndex(index)
		if self.data[self.rightChildIndex(index)] > self.data[self.leftChildIndex(index)]:
			return self.rightChildIndex(index)
		else:
			return self.leftChildIndex(index)

	def delete(self):
		self.data[0] = self.data.pop()
		trickle_node_index = 0

		while self.hasGreaterChild(trickle_node_index):
			larger_child_index = self.calculateLargerChild(trickle_node_index)

			self.data[trickle_node_index], self.data[larger_child_index] = self.data[larger_child_index], self.data[trickle_node_index]
			trickle_node_index = larger_child_index
		