# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 21:07:47 2024

@author: Rosshun
"""
def find_zero_sum_subarrays(arr):
    n = len(arr)
    res = []
    sum_map = {0:[-1]}  #to handle subarrays that start from index 0 and sum to zero.
    cum_sum = 0
    
    for i in range(n):
        cum_sum += arr[i]
        if cum_sum in sum_map:
            for start in sum_map[cum_sum]:
                res.append((start+1,i))
        sum_map[cum_sum] = sum_map.get(cum_sum,[]) + [i]
    
    return res

arr = eval(input("Input: "))
print("Ouput: ",find_zero_sum_subarrays(arr))