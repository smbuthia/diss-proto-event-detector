__author__ = 'smbuthia'


class BinarySearchTree:
    """Code for binary search tree"""

    root = None
    dict_list = dict([])

    def insert(self, key):
        y = None
        x = self.root
        while x is not None:
            y = x
            if key < x.key:
                x = x.left
            else:
                x = x.right
        if y is None:
            self.root = Node(key, None, None, None)
        elif key < y.key:
            y.left = Node(key, y, None, None)
        elif key > y.key:
            y.right = Node(key, y, None, None)
        elif key == y.key:
            y.value += 1

    def transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v is not None:
            v.parent = u.parent

    def remove(self, x, key):
        z = self.find(x, key)
        if z.left is None:
            self.transplant(z, z.right)
        elif z.right is None:
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            if y.parent != z:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y

    def maximum(self, x):
        if x.right is not None:
            return self.maximum(x.right)
        return x

    def minimum(self, x):
        if x.left is not None:
            return self.minimum(x.left)
        return x

    def successor(self, key):
        x = self.find(self.root, key)
        if x.right is not None:
            return self.minimum(x.right)
        y = x.parent
        while y is not None and x == y.right:
            x = y
            y = y.parent
        return y

    def predecessor(self, key):
        x = self.find(self.root, key)
        if x.left is not None:
            return self.maximum(x.left)
        y = x.parent
        while y is not None and x == y.left:
            x = y
            y = y.parent
        return y

    def find(self, x, key):
        if x is None or x.key == key:
            return x
        if key < x.key:
            return self.find(x.left, key)
        else:
            return self.find(x.right, key)

    def in_order_tree_walk(self, x):
        if x is not None:
            self.in_order_tree_walk(x.left)
            print("{k} - {v} \n".format(k=x.key,v=x.value))
            self.in_order_tree_walk(x.right)

    def tree_to_list(self, x):
        if x is not None:
            self.tree_to_list(x.left)
            self.dict_list[x.key] = x.value
            self.tree_to_list(x.right)


class Node:
    """Code for single node"""
    def __init__(self, key, parent, left, right):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right
        self.value = 1

#tree = BinarySearchTree()
#nums = ['tree', 'man', 'bat', 'tree', 'quit', 'for', 'for', 'quit', 'it', 'tree']
#for num in nums:
    #tree.insert(num)

#print(tree.maximum(tree.root).key)
#tree.in_order_tree_walk(tree.root)