# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 16:47:43 2024

@author: Rosshun
"""
def repeating_number(arr):
    n=len(arr)-1  #since the arr has n+1 elements with element missing
    expected_sum=(n*(n+1))//2 #Sum of AP of n numbers.(// is used to avoid Decimal caused by repeating number)
    actual_sum=sum(arr)
    repeating_number=actual_sum-expected_sum
    return repeating_number

arr=eval(input("Input: "))
print("Output: ",repeating_number(arr))