from itertools import imap, ifilterfalse
import tree

def _pathlist(inst_name):
    if inst_name.startswith('PAD'):
        return ['pad', inst_name, 'pad']
    elif inst_name.startswith('hevc_clk'):
        return ['clk', inst_name]
    else:
        return inst_name.split('/')

def _getleaf(line):
    li = line.split()
    # instance, internal, switching, total, leakage, module = li
    return (_pathlist(li[0]), float(li[3]))

def _removeline(line):
    return line.startswith('*')

def parsereport(file_name):
    root = tree.Tree()
    fin = open(file_name, 'r')
    addleaf = root.addleaf
    for (path, val) in imap(_getleaf, ifilterfalse(_removeline, fin)):
        addleaf(path, val)
    return root
