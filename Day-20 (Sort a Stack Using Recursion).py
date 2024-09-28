# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 17:03:50 2024

@author: Rosshun
"""
def recur_sort(stack):
    if not stack:
        return stack

    current_element = stack.pop()
    stack = recur_sort(stack)
    insert_element(stack, current_element)
    return stack


def insert_element(stack, element):
    if not stack or element >= stack[-1]:
        stack.append(element)
    else:
        nxt_element = stack.pop()
        insert_element(stack, element)
        stack.append(nxt_element)

arr = eval(input("Input: "))
print("Output:", recur_sort(arr))
