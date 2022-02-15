from multiprocessing.sharedctypes import Value


class TreeNode:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

def search(searchValue, node):
	if node is None or node.val == searchValue:
		return node
	elif searchValue < node.val:
		search(searchValue, node.left)
	else:
		search(searchValue, node.right)

def insertion(value, node):
	if value < node.val:
		if node.left is None:
			node.left = TreeNode(value)
		else:
			insertion(value, node.left)
	elif value > node.val:
		if node.right is None:
			node.right = TreeNode(value)
		else:
			insertion(value, node.right)

def lift(node, nodeToDelete):
	if node.left:
		node.left = lift(node.left, nodeToDelete)
		return node
	else:
		nodeToDelete.val = node.val
		return node.right

def delete(valueToDelete, node):
	if node is None:
		return None
	elif valueToDelete < node.val:
		node.left = delete(valueToDelete, node.left)
		return node
	elif valueToDelete > node.val:
		node.right = delete(valueToDelete, node.right)
		return node
	elif valueToDelete == node.val:
		if node.left is None:
			return node.right
		elif node.right is None:
			return node.left
		else:
			node.right = lift(node.right, node)
			return node

def traverse(node):
	if node is None:
		return
	traverse(node.left)
	print(node.val)
	traverse(node.right)

def findGreatest(node):
	if node.right:
		return findGreatest(node.right)
	else:
		return node.val
	