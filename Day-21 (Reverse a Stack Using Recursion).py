# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 20:07:53 2024

@author: Rosshun
"""
def insert_at_bottom(stack, element):
    if not stack:
        stack.append(element)
    else:
        temp = stack.pop()
        insert_at_bottom(stack, element)
        stack.append(temp)

def reverse_stack(stack):
    if stack:
        temp = stack.pop()
        reverse_stack(stack)
        insert_at_bottom(stack, temp)

arr = eval(input("Input: "))
print("Output:", reverse_stack(arr))
