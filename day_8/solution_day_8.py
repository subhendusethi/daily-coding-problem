class Node:
	def __init__(self, val, left:'Node'=None, right:'Node'=None):
		self.val = val
		self.left = left
		self.right = right
		self.sub_val = None
		self.is_sub_val = False
'''
	Time Complexity: O(N) 
	Space Complexity: O(N) (Can be reduced to O(1) by returning sub_val
							and is_sub_val at every step of recursion to parent.)
	N : Number of nodes in the tree
'''
class Day8:
	def execute(self, head):
		if head == None:
			return 0
		if head.left == None and head.right == None:
			head.sub_val = 1
			head.is_sub_val = True
			return 1
		res = 0
		if head.left:
			self.execute(head.left)
			res+=head.left.sub_val
		if head.right:
			self.execute(head.right)
			res+=head.right.sub_val
		if head.left and head.right and head.left.val == head.right.val == head.val and head.left.is_sub_val and head.right.is_sub_val:
			res+=1
			head.is_sub_val = True
		if head.left == None and head.right.val == head.val and head.right.is_sub_val:
			res+=1
		if head.right == None and head.left.val == head.val and head.left.is_sub_val:
			res+=1
		head.sub_val = res
		return res

day_8 = Day8()

node = Node(1, Node(1, Node(1), Node(1,Node(1,Node(1), Node(1)),Node(1))),  Node(1, Node(1), Node(1,Node(1,Node(1), Node(1)),Node(1))))
assert day_8.execute(node) == 15

node = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0))) 
assert day_8.execute(node) == 5

node = Node(0)
assert day_8.execute(node) == 1

node = None
assert day_8.execute(node) == 0
