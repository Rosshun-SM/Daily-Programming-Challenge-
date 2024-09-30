# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 20:54:50 2024

@author: Rosshun
"""
def first_k_times(nums, k):
    freq = {}
    for val in nums:
        freq[val] = freq.get(val,0)+1
    for val in nums:
        if freq[val] == k:
            return val
    return -1

arr = eval(input("Input: arr = "))
k = int(input("       k = "))
print("Output:", first_k_times(arr,k))


