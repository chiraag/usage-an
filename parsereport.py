from itertools import ifilterfalse
import tree

def _ancestor_update(node, leaf_val):
    total, local = node.value
    node.value = total + leaf_val, local 

def _parent_update(node, leaf_val):
    total, local = node.value
    node.value = total + leaf_val, local + leaf_val

_tree_class = tree.tree((0 , 0), _parent_update, _ancestor_update)

def branches(node):
    return (it for it in node.iteritems() if isinstance(it[1], _tree_class))

def tree_from_report(file_name):
    def pathlist(inst_name):
        if inst_name.startswith('PAD'):
            return ['pad', inst_name, 'pad']
        elif inst_name.startswith('hevc_clk'):
            return ['clk', inst_name]
        else:
            return inst_name.split('/')

    root = _tree_class()
    addleaf = root.insertnode
    
    fin = open(file_name, 'r')
    
    for l in ifilterfalse(lambda l: l.startswith('*'), fin):
        li = l.split()
        addleaf(node_path=pathlist(li[0]), node_val=float(li[3]))
    
    return root
