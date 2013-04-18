from itertools import imap, ifilterfalse
import tree

def _pathlist(inst_name):
    if inst_name.startswith('PAD'):
        return ['pad', inst_name, 'pad']
    elif inst_name.startswith('hevc_clk'):
        return ['clk', inst_name]
    else:
        return inst_name.split('/')

def _ancestor_update(node, leaf_val):
    total, local = node.value
    node.value = total + leaf_val, local 

def _parent_update(node, leaf_val):
    total, local = node.value
    node.value = total + leaf_val, local + leaf_val

def _getleaf(line):
    li = line.split()
    # instance, internal, switching, total, leakage, module = li
    return _pathlist(li[0]), float(li[3])

def _removeline(line):
    return line.startswith('*')

def parsereport(file_name):
    tree_class = tree.tree((0 , 0), _parent_update, _ancestor_update)
    
    root = tree_class()
    addleaf = root.addleaf
    
    fin = open(file_name, 'r')
    
    for leaf in imap(_getleaf, ifilterfalse(_removeline, fin)):
        addleaf(*leaf)
    
    return root
