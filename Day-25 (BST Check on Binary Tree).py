# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 23:02:33 2024

@author: Rosshun
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isValidBST(root: TreeNode) -> bool:
    def helper(node, lower=float('-inf'), upper=float('inf')):
        if not node:
            return True

        val = node.val
        if val <= lower or val >= upper:
            return False

        if not helper(node.right, val, upper):
            return False
        if not helper(node.left, lower, val):
            return False

        return True

    return helper(root)

def list_to_tree(arr):
    if not arr or arr[0] is None:
        return None

    root = TreeNode(arr[0])
    q = [root]
    idx = 1

    while idx < len(arr):
        curr = q.pop(0)
        if idx < len(arr) and arr[idx] is not None:
            curr.left = TreeNode(arr[idx])
            q.append(curr.left)
        idx += 1
        if idx < len(arr) and arr[idx] is not None:
            curr.right = TreeNode(arr[idx])
            q.append(curr.right)
        idx += 1

    return root

input_str = input("Input: root = ")
# Clean input and handle array parsing
arr = [int(x.strip()) if x.strip() != 'null' else None for x in input_str.strip('[]').split(',')]
root = list_to_tree(arr)

is_bst = isValidBST(root)
print("Output:", is_bst)
