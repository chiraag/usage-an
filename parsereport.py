""" 
Every node in the tree has a local value which is the sum of all 
leaves at that node and a total value which is sum of the local value
total values of all its branches 
"""
from itertools import ifilterfalse
import tree

# def sum_values(tree):
# 		tree_value[0] += tree_value[1]
# 		for node in tree:
# 				sum_values(tree[node])
# 				final_value[0] += tree[node].value[0]

def branches(node):
    return (it for it in node.iteritems() if isinstance(it[1], _tree_class))

def tree_from_report(file_name):
    def pathlist(inst_name):
			  return inst_name.split('/')

    usage_tree = tree.Tree_Obj()
    fin = open(file_name, 'r')
    
    for line in fin:
        line = line.rstrip()
        tags = line.split(None, 1)
        # print tags[1]
        usage_tree.insertnode(node_path=pathlist(tags[1]), node_val=(tags[0]))
    
    return usage_tree
