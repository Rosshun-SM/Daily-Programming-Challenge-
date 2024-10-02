# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 12:46:10 2024

@author: Rosshun
"""
class Node:
    def __init__(self, k):
        self.k = k
        self.l = None
        self.r = None

def find_path(r, path, k):
    if r is None:
        return False

    path.append(r)

    if r.k == k:
        return True

    if ((r.l is not None and find_path(r.l, path, k)) or
            (r.r is not None and find_path(r.r, path, k))):
        return True

    path.pop()
    return False

def find_lca(r, n1, n2):
    path1 = []
    path2 = []

    if (not find_path(r, path1, n1) or not find_path(r, path2, n2)):
        return None

    i = 0
    while(i < len(path1) and i < len(path2)):
        if path1[i].k != path2[i].k:
            break
        i += 1
    return path1[i-1] if i > 0 else None

def list_to_tree(arr):
    if not arr or arr[0] is None:
        return None

    root = Node(arr[0])
    q = [root]
    idx = 1

    while idx < len(arr):
        curr = q.pop(0)
        if idx < len(arr) and arr[idx] is not None:
            curr.l = Node(arr[idx])
            q.append(curr.l)
        idx += 1
        if idx < len(arr) and arr[idx] is not None:
            curr.r = Node(arr[idx])
            q.append(curr.r)
        idx += 1

    return root


input_str = input("Input: arr = ")
arr = [int(x.strip()) if x.strip() != 'null' else None for x in input_str[1:-1].split(',')]
root = list_to_tree(arr)

p = int(input("       p = "))
q = int(input("       q = "))

lca = find_lca(root, p, q)
print("Output:", lca.k if lca is not None else None)