class Node:
	def __init__(self, val, left:'Node'=None, right:'Node'=None):
		self.val = val
		self.left = left
		self.right = right
'''
	Time Complexity: O(N) 
	Space Complexity: O(H) 
	N : Number of nodes in the tree
	H : Height of the tree.
'''
class Day8:
	def execute(self, head):
		count, _ = self.__execute_helper(head)
		return count
	def __execute_helper(self, node):
		if node == None:
			return 0, True
		if node.left == None and node.right == None:
			return 1, True
		res = 0
		curr_is_sub_val = False
		left_res, left_is_sub_val = None, False
		right_res, right_is_sub_val = None, False
		if node.left:
			left_res, left_is_sub_val = self.__execute_helper(node.left)
			res+=left_res
		if node.right:
			right_res, right_is_sub_val = self.__execute_helper(node.right)
			res+=right_res
		if node.left and node.right \
		and node.left.val == node.right.val == node.val \
		and left_is_sub_val and right_is_sub_val:
			res+=1
			curr_is_sub_val = True
		if node.left == None and node.right.val == node.val and right_is_sub_val:
			res+=1
			curr_is_sub_val = True
		if node.right == None and node.left.val == node.val and left_is_sub_val:
			res+=1
			curr_is_sub_val = True
		return res, curr_is_sub_val

day_8 = Day8()

node = Node(1, Node(1, Node(1), Node(1,Node(1,Node(1), Node(1)),Node(1))),  Node(1, Node(1), Node(1,Node(1,Node(1), Node(1)),Node(1))))
assert day_8.execute(node) == 15

node = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0))) 
assert day_8.execute(node) == 5
assert day_8.execute(node.left) == 1
assert day_8.execute(node.right) == 4
assert day_8.execute(node.right.left) == 3

node = Node(0)
assert day_8.execute(node) == 1

node = None
assert day_8.execute(node) == 0