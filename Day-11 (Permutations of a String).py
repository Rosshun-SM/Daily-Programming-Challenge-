# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 16:51:43 2024

@author: Rosshun
"""
def swap(s,i,j):
    s = list(s)
    s[i], s[j] = s[j], s[i]
    return ''.join(s)

def permute_rec(s,idx,result,seen):    
    if idx == len(s)-1:
        result.append(s)
        return
    
    for i in range(idx,len(s)):        
        if s[i] in seen:
            continue
        
        seen.add(s[i])  #add is used for appending in set
        s = swap(s,idx,i)        
        permute_rec(s,idx+1,result,set())    #Recursive function
        s = swap(s,idx,i)

def permute(s):
    result = []
    permute_rec(s,0,result,set())  #a set only accepts unique values
    return result

s = input("Input: ")
print("Ouput: ",permute(s))
