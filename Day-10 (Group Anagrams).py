# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 09:02:28 2024

@author: Rosshun
"""
def group_anagrams(strs):
    anagrams = {}
    
    for word in strs:
        sort_word = ''.join(sorted(word)) #Sort the words
        
        if sort_word in anagrams:  #To add word to its anagram
            anagrams[sort_word].append(word)
        else:
            anagrams[sort_word] = [word]
    
    return list(anagrams.values())

strs = eval(input("Input: strs[] = "))
print("Ouput: ", group_anagrams(strs))