# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 19:56:39 2024

@author: Rosshun
"""
def leader_arr(arr):
    l = len(arr)
    if l == 0: 
        return []
    leadarr = []
    leader = arr[-1]  #Since last element is always a leader.
    leadarr.append(leader) 
    
    for i in range(l-2,-1,-1): #We iterate from right to left and find the largest number along the way.
        if arr[i]>leader:
            leader = arr[i]
            leadarr.append(leader)
    
    leadarr.reverse()  #We reverse since we iterate from right to left.
    return leadarr
    
arr = eval(input("Input: "))
print("Ouput: ",leader_arr(arr))
