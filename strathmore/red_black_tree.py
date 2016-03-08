import random

__author__ = 'smbuthia'


class RedBlackTree:
    """Code implementation for red-black tree"""

    def __init__(self):
        self.root = Node(None, None, None, None)

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left.key is not None:
            y.left.parent = x
        y.parent = x.parent
        if x.parent.key is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if x.left.key is not None:
            y.right.parent = x
        y.parent = x.parent
        if x.parent.key is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = x
        else:
            x.parent.right = y
        y.right = x
        x.parent = y

    def insert(self, key):
        z = Node(key, None, None, None)
        y = Node(None, None, None, None)
        x = self.root
        while x.key is not None:
            y = x
            if key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y.key is None:
            self.root = z
        elif key < y.key:
            y.left = z
        else:
            y.right = z
        z.left = Node(None, z, None, None)
        z.right = Node(None, z, None, None)
        z.color = 'red'
        self.insert_fix_up(z)

    def insert_fix_up(self, z):
        while z.parent.color == 'red' and z.parent.key is not None:
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == 'red':
                    z.parent.color = 'black'
                    y.color = 'black'
                    z.parent.parent.color = 'red'
                    z = z.parent.parent
                elif z == z.parent.right:
                    z = z.parent
                    self.left_rotate(z)
                z.parent.color = 'black'
                if z.parent.key is not None:
                    z.parent.parent.color = 'red'
                    if z.parent.parent.key is not None:
                        self.right_rotate(z.parent.parent)
            elif z.parent == z.parent.parent.right:
                y = z.parent.parent.left
                if y.color == 'red':
                    z.parent.color = 'black'
                    y.color = 'black'
                    z.parent.parent.color = 'red'
                    z = z.parent.parent
                elif z == z.parent.left:
                    z = z.parent
                    self.right_rotate(z)
                z.parent.color = 'black'
                if z.parent.key is not None:
                    z.parent.parent.color = 'red'
                    if z.parent.parent.key is not None:
                        self.left_rotate(z.parent.parent)
        self.root.color = 'black'

    def find(self, x, key):
        if x.key is None or x.key == key:
            return x
        if key < x.key:
            return self.find(x.left, key)
        else:
            return self.find(x.right, key)


class Node:
    """Code for single node"""
    def __init__(self, key, parent, left, right):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right
        self.value = 1
        self.color = 'black'


tree = RedBlackTree()
#nums = [7, 8, 9, 10]
for i in range(100):
    tree.insert(i+1)
#for num in nums:
    #tree.insert(num)

print(tree.root.key)
#print(tree.find(tree.root, 2).right.right.right.key)


