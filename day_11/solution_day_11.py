from typing import List
import os

dirname = os.path.dirname(__file__)

VectorString = List[str]

class Node:
	def __init__(self, val:str, endpoint:bool=False):
		self.val = val
		self.children = []
		self.endpoint = endpoint

class Trie:
	def __init__(self):
		self.head = Node("")
	def add_word(self, word:str):
		word_char_list = word.split()
		curr_node = self.head
		for i in range(len(word)):
			curr_char = word[i]
			curr_node = self.__add_char_at_node(curr_node, curr_char)
		curr_node.endpoint = True
	def __add_char_at_node(self, node:'Node', char:str) -> 'Node':
		for child in node.children:
			if child.val == char:
				return child
		new_node = Node(char)
		node.children.append(new_node)
		return new_node
	def __find_node_by_prefix(self, node:'Node', prefix:str) -> 'Node':
		if len(prefix) == 0:
			return node
		else:
			for child in node.children:
				if child.val == prefix[0]:
					return self.__find_node_by_prefix(child, prefix[1:])
					break
			return None
	def print_auto_completed_words(self, prefix:str):
		prefix_node = self.__find_node_by_prefix(self.head, prefix)
		self.__print_at_node(prefix_node, prefix[:-1])

	def __print_at_node(self, node:'Node', prefix:str=""):
		self.__print_at_node_helper(node, prefix)
	def print_at_head(self):
		self.__print_at_node(self.head)
	def __print_at_node_helper(self, node:'Node', prefix:str):
		if node == None:
			return
		if node.endpoint:
			print(prefix + node.val)
		new_prefix = prefix + node.val
		for child_node in node.children:
			self.__print_at_node_helper(child_node, new_prefix)

trie = Trie()
corpus_filename = os.path.join(dirname, './corpus.txt')
with open(corpus_filename, 'r+') as file:
	for line in file:
		trie.add_word(line.strip('\n'))

while True:
	query = input()
	trie.print_auto_completed_words(query)