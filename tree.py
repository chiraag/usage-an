class Tree(dict):
    """ Every node in the tree has a local value which is the sum of all 
    leaves at that node and a total value which is sum of the local value
    total values of all its branches """
    def __init__(self):
        self.total = 0
        self.local = 0

    def __missing__(self, key):
        t = Tree()
        self[key] = t
        return t

    def addleaf(self, leaf_path, val):
        " Add a leaf given as [root, br1, br2, ... leaf_name] to the tree"
        node = self
        for br_name in leaf_path[:-1]:
            node.total += val
            node = node[br_name]

        leaf_name = leaf_path[-1]

        if leaf_name in node:
            # Error if leaf already exists
            node = self
            for br_name in leaf_path[:-1]:
                node.total -= val
                node = node[br_name]
            raise ValueError('/'.join(leaf_path) + ' already exists')
        else:
            node.total += val
            node.local += val
            node[leaf_name] = val

    def iterbranches(self):
        " Filter out the leaves at the node"
        return (it for it in self.iteritems() if isinstance(it[1], Tree))
