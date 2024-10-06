# -*- coding: utf-8 -*-
"""
Created on Sat Oct 5 20:49:43 2024

@author: Rosshun
"""
from collections import deque

def shortest_path(V, edges, start, end):
    adj_list = [[] for _ in range(V)]
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)

    queue = deque([(start, 0)])  
    visited = [False] * V
    visited[start] = True

    while queue:
        node, dist = queue.popleft()
        if node == end:
            return dist

        for neighbor in adj_list[node]:
            if not visited[neighbor]:
                queue.append((neighbor, dist + 1))
                visited[neighbor] = True

    return -1  


V = int(input("V = "))
edges = eval(input("edges = "))
start = int(input("start = "))
end = int(input("end = "))

print("Ouput =",shortest_path(V, edges, start, end))