# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 19:11:34 2024

@author: Rosshun
"""
def expand_center(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left +1: right]

def longest_palindrome(s):
    if (len(s) == 1) or (len(set(s)) == 1) or (len(s) ==0):
        return s
    
    longest_palindrome = ""
    
    for i in range(len(s)):
        
        odd_palindrome = expand_center(s, i, i)
        if len(longest_palindrome) < len(odd_palindrome):
            longest_palindrome = odd_palindrome            
                   
        even_palindrome = expand_center(s, i, i+1)
        if len(longest_palindrome) < len(even_palindrome):
            longest_palindrome = even_palindrome   
    
    return longest_palindrome


s = input("Input: ")
print("Output:", longest_palindrome(s))