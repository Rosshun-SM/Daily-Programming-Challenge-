# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 14:28:58 2024

@author: Rosshun
"""
def most_k_chars(s, k):
    if not s:
        return 0
    
    table = {}
    num = 0
    left = 0
    
    for i, c in enumerate(s):
        table[c] = table.get(c, 0) + 1
        while len(table) > k:
            table[s[left]] -= 1
            if table[s[left]] == 0:
                del table[s[left]]
            left += 1
        num += i - left + 1
    return num

def count_k_chars(s, k):
    return most_k_chars(s, k) - most_k_chars(s, k - 1)

s = input("Input: s = ")
k = int(input("       k = "))
print("Ouput:", count_k_chars(s, k))