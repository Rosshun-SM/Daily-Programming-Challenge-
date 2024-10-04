# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 20:27:31 2024

@author: Rosshun
"""
def hasCycle(V, E, edges):
    graph = [[] for _ in range(V)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * V

    for i in range(V):
        if not visited[i]:
            if dfs(i, -1, graph, visited):  
                return True

    return False

def dfs(vertex, parent, graph, visited):
    visited[vertex] = True

    for neighbor in graph[vertex]:
        if not visited[neighbor]:
            if dfs(neighbor, vertex, graph, visited):
                return True
        elif neighbor != parent:  
            return True

    return False


V = int(input("V = "))
E = int(input("E = "))
edges = eval(input("Edges = "))

print("Output:", "true" if hasCycle(V, E, edges) else "false")