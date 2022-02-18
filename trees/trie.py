class TrieNode:
	def __init__(self):
		self.children = {}

class Trie:
	def __init__(self):
		self.root = TrieNode()

	def search(self, searchWord):
		current_node = self.root
		for c in searchWord:
			if current_node.children.get(c):
				current_node = current_node.children[c]
			else:
				return None
		
		return current_node

	def insertion(self, word):
		current_node = self.root
		for c in word:
			if current_node.children.get(c):
				current_node = current_node.children[c]
			else:
				new_node = TrieNode()
				current_node.children[c] = new_node
				current_node = new_node
		current_node.children['*'] = None