from dataclasses import dataclass

from more_itertools import first


class Node:
	next_node = None
	prev_node = None
	def __init__(self, data, next_node=None, prev_node=None):
		self.data = data
		self.next_node = next_node
		self.prev_node = prev_node
			
class DoublyLinkedList:
	head = None
	tail = None
	def __init__(self, first_node=None, last_node=None):
		self.head = first_node
		self.tail = last_node
	def insertAtEnd(self, value):
		newNode = Node(value)
		if not self.head:
			self.head = newNode
			self.tail = newNode
		else:
			newNode.prev_node = self.tail
			self.tail.next_node = newNode
			self.tail = newNode
	def deleteFromFront(self):
		removedNode = self.head
		self.head = self.head.next_node
		return removedNode
	# Question 2
	def printAllReverse(self):
		if not self.tail:
			print(None)
			return
		else:
			current_node = self.tail
			while current_node:
				print(current_node.data)
				current_node = current_node.prev_node

class Queue:
	def __init__(self):
		self.data = DoublyLinkedList()
	def enqueue(self, element):
		self.data.insertAtEnd(element)
	def dequeue(self):
		self.data.deleteFromFront()
	def read(self):
		if self.head == None:
			return None
		return self.head.data	


dl = DoublyLinkedList()
dl.insertAtEnd(1)
dl.insertAtEnd(2)
dl.insertAtEnd(3)

dl.printAllReverse()