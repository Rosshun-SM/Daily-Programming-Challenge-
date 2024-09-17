# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 21:33:19 2024

@author: Rosshun
"""
def long_Com_Pref(strs):
    if not strs: #For empty array
        return ""
    
    prefix = strs[0] #Set the first string as the prefix
    
    for s in strs[1:]: #caompare prefix with each string
        while not s.startswith(prefix): #To check whether a string starts with the prefix
            prefix = prefix[:-1]
            
            if not prefix:
                return ""
    
    return prefix

strs = eval(input("Input: strs[] = "))
print("Ouput: ", long_Com_Pref(strs))