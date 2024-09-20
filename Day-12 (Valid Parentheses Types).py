# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 17:35:13 2024

@author: Rosshun
"""
def valid_parentheses(s):
    
    par_map = {'(':')', '[':']', '{':'}'}
    
    stack = []   #empty stack 
    if not s:
        return "true"
    elif (len(s)%2 != 0) or (s[0] in par_map.values()):
        return "false"
    
    for char in s:
        if char in par_map:
            stack.append(char)
            
        elif char in par_map.values():
            if (not stack) or (char != par_map[ stack.pop() ]):
                return "false"
    
    if not stack: return "true" 
    else: return "false" 

s = input("Input: s = ")
print("Output: ",valid_parentheses(s))