# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 17:36:30 2024

@author: Rosshun
"""
def missing_number(arr):
    n=len(arr)+1  #since the arr has n-1 elements with element missing
    expected_sum=(n*(n+1))//2 #Sum of AP of n numbers.(// is used to avoid Decimal caused by missing number)
    actual_sum=sum(arr)
    missing_number=expected_sum-actual_sum
    return missing_number

arr=eval(input("Enter the array to find the missing element from.\n: "))
print(missing_number(arr))
