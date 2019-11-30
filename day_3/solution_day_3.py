class Node(object):
	def __init__(self, val: str, left: 'Node'= None, right: 'Node'=None):
		self.val = val
		self.left = left
		self.right = right

node_separator = "$"
value_level_separator = "_"

def serialize(node: 'Node') -> str:
	return serialize_helper(node,1)

'''
	While serializing store the level of each node along 
	with the node value in a in order traversal.
	
	A node with index N will have its children as [ 2*N ] and [ (2*N) + 1 ]

	e.g: for Node('root', Node('left', Node('left.left')), Node('right'))
	we get: $left.left_4$left_2$root_1$right_3

'''
def serialize_helper(node: 'Node', level: int) -> str:
	if node == None:
		return ""
	if node.left == None and node.right == None:
		return node_separator + node.val + "_" + str(level)
	return serialize_helper(node.left, 2*level) + node_separator + node.val + value_level_separator + str(level) + serialize_helper(node.right, 2*level + 1)

def deserialize(s: str) -> 'Node':
	if len(s) == 0:
		return None
	s_list = s.split(node_separator)
	level_node_mapping = {}
	for x in s_list:
		if len(x) == 0:
			continue
		# item : [node_value , node_level]
		item = x.split(value_level_separator)
		level_node_mapping[int(item[1])] = Node(item[0])
	for x in level_node_mapping.keys():
		if 2*x in level_node_mapping:
			level_node_mapping[x].left = level_node_mapping[2*x]
		if 2*x + 1 in level_node_mapping:
			level_node_mapping[x].right = level_node_mapping[2*x + 1]
	return level_node_mapping[1]

node = Node('root', Node('left', Node('left.left', Node('left.left.left'), Node('left.left.right'))), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
assert deserialize(serialize(node)).left.left.right.val == 'left.left.right'
assert deserialize(serialize(node)).left.left.left.val == 'left.left.left'
assert deserialize(serialize(node.left.left.right)).val == 'left.left.right'