# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 21:05:47 2024

@author: Rosshun
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def list_to_tree(lst):
    if not lst:
        return None
    nodes = [TreeNode(x) if x is not None else None for x in lst]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root

def is_symmetric(root):
    def is_mirror(t1, t2):
        if t1 is None and t2 is None:
            return True
        if t1 is None or t2 is None:
            return False
        return (t1.val == t2.val) and is_mirror(t1.right, t2.left) and is_mirror(t1.left, t2.right)

    return is_mirror(root, root)


input_str = input("Input: ")
arr = [int(x) if x != 'null' and x != '' else None for x in input_str.replace(' ', '').strip('[]').split(',')]
root = list_to_tree(arr)
print("Output:", is_symmetric(root))