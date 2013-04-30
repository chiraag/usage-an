class Tree_Obj(dict):
	def __init__(self):
		self.name = None
		self.value = None
	
	def __missing__(self, key):
		t = Tree_Obj()
		self[key] = t
		return t
	
	def insertnode(self, node_path, node_val):
		""" 
		Add a node with path given as list of successive indices.
		Also, the parent is modified by parent_update(node_val)
		All other ancestors' are modified by ancestor_update(node_val)
		"""
		# Get to the correct tree
		curr_tree = self
		for node_name in node_path[1:]:
			curr_tree = curr_tree[node_name]
		
		# Allocate to tree (only once)
		if curr_tree.name == None:
			curr_tree.name = node_path[-1]
			curr_tree.value = node_val
		else:
			print curr_tree.name
			print node_path
			assert(False)
