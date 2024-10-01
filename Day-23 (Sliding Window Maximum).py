# -*- coding: utf-8 -*-
"""
Created on Sat Oct 1 15:00:36 2024

@author: Rosshun
"""
from collections import deque

def max_slid_win(nums,k):
    deq, max_vals = deque(),[]
    
    for idx, num in enumerate(nums):
        if deq and deq[0] < idx-k+1:
            deq.popleft()
        
        while deq and nums[deq[-1]] < num:
            deq.pop()
        
        deq.append(idx)
        
        if idx >= k-1:
            max_vals.append(nums[deq[0]])
    
    return max_vals

arr = eval(input("Input: arr = "))
k = int(input("       k = "))
print("Output:", max_slid_win(arr,k))
