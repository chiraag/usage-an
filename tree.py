def _do_nothing(x, y): pass

def tree(init_val=None, parent_update=_do_nothing, ancestor_update=_do_nothing):
    class MyTree(dict):
        _init_val = init_val
        _parent_upd = parent_update
        _ancestor_upd = ancestor_update

        def __init__(self):
            self.value = init_val
            self.parents = []

        def __missing__(self, key):
            t = MyTree()
            t.parents.append(self)
            self[key] = t
            return t
        
        def insertnode(self, node_path, node_val):
            """ 
            Add a node with path given as list of successive indices.
            Also, the parent is modified by parent_update(node_val)
            All other ancestors' are modified by ancestor_update(node_val)
            """
            # Get parent of node to be added
            parent = self
            for br_name in node_path[:-1]:
                parent._ancestor_upd(node_val)
                parent = parent[br_name]

            node_name = node_path[-1]

            # Error if node already exists
            if node_name in parent:
                raise ValueError('{} already exists'.format(node_path))
            else:
                parent._parent_upd(node_val)
                parent[node_name] = node_val
                # Try to register parent in node_val's list of parents
                try:
                    node_val.parents.append(parent)
                except AttributeError:
                    pass
   
    return MyTree
