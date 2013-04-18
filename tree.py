def tree(init_val, parent_update=lambda: None, ancestor_update=lambda: None):
    class MyTree(dict):
        """ 
        Every node in the tree has a local value which is the sum of all 
        leaves at that node and a total value which is sum of the local value
        total values of all its branches 
        """
        _init_val = init_val
        _parent_upd = parent_update
        _ancestor_upd = ancestor_update

        def __init__(self):
            self.value = init_val

        def __missing__(self, key):
            t = MyTree()
            self[key] = t
            return t
        
        def addleaf(self, leaf_path, leaf_val):
            """ 
            Add a leaf given as [root, br1, br2, ... leaf_name] to the tree.
            leaf_val is added as an entry to its parent tree dict.
            Also, the parent is modified by parent_update(leaf_val)
            All other ancestors' are modified by ancestor_update(leaf_val)
            """

            node = self
            for br_name in leaf_path[:-1]:
                node._ancestor_upd(leaf_val)
                node = node[br_name]
                if not isinstance(node, MyTree):
                    raise ValueError('Trying to add a leaf as child to another leaf')

            leaf_name = leaf_path[-1]

            if leaf_name in node:
                # Error if leaf already exists
                raise ValueError('{} already exists'.format(leaf_path))
            else:
                node._parent_upd(leaf_val)
                node[leaf_name] = leaf_val

        def iterbranches(self):
            " Filter out the leaves at the node"
            return (it for it in self.iteritems() if isinstance(it[1], MyTree))
        
        def iterleaves(self):
            " Filter out the branches at the node"
            return (it for it in self.iteritems() if not isinstance(it[1], MyTree))
    
    return MyTree
