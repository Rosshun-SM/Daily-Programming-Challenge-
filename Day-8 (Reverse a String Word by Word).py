# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 23:03:54 2024

@author: Rosshun
"""
def reverse_words(s:str)->str:
    s=s.strip()  # all leading and trailing spaces are removed
    words=s.split() #converted to array with each word
    reversed_words=words[::-1]  # words are reversed
    return ' '.join(reversed_words)  # Words are joined into a single string with single space

user_input = input("Input: ")  
print("Output: ", reverse_words(user_input)) 