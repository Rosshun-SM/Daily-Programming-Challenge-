# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 23:12:23 2024

@author: Rosshun
"""
def sort(arr):
    low, mid, high = 0, 0, len(arr) - 1
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr

# Example usage
arr = [0, 1, 2, 1, 0, 2, 1, 0]
print(sort(arr))
