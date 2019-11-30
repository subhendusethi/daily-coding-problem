class Node:
	def __init__(self, value:int, both:int = None):
		self.value = value
		self.both = both

class Day6:
	def __init__(self):
		self.head = None
	def __dereference_pointer(self, value:int) -> 'Node':
		pass
	def __get_pointer(self, node:'Node') -> 'int':
		pass
	'''
		a^(a^b) = (a^a)^b = b
		https://accu.org/index.php/journals/1915
	'''
	def add(element:int):
		if self.head == None:
			self.head = Node(element)
			self.head.both = 1^self.__get_pointer(self.head)
		else:
			curr_pointer = self.__dereference_pointer(self.head)
			prev_node_deref = 1
			while curr_pointer.both != curr_pointer:
				next_node_pointer = self.__dereference_pointer(prev_node_deref^curr_pointer.both)
				prev_node_deref = curr_pointer
				curr_pointer = next_node_pointer
			new_node = Node(element)
			curr_pointer.both = curr_pointer.both ^ self.__get_pointer(new_node)
			new_node.both = self.__get_pointer(new_node)
	def get(index:int) -> 'Node':
		curr_pointer = self.__dereference_pointer(self.head)
		prev_node_deref = 1
		curr_index = 0
		while curr_pointer.both != curr_pointer:
			if curr_index == index:
				return curr_pointer
			next_node_pointer = self.__dereference_pointer(prev_node_deref^curr_pointer.both)
			prev_node_deref = curr_pointer
			curr_pointer = next_node_pointer
		return None

