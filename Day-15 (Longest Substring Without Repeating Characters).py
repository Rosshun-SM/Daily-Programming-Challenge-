# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 19:00:39 2024

@author: Rosshun
"""
def longest_substring(s):
    current_set = set()
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        while s[right] in current_set:
            current_set.remove(s[left])
            left += 1
        current_set.add(s[right])
        max_length = max(max_length, right-left+1)
    
    return max_length

s = input("Input: S = ") 
print("Ouput:", longest_substring(s))