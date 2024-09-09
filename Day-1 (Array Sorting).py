# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 23:20:17 2024

@author: Rosshun
"""
def sort(arr):
    low,mid,high = 0,0,len(arr) - 1
    while mid<=high:
        if arr[mid]==0:
            arr[low],arr[mid]=arr[mid],arr[low]
            low+=1
            mid+=1
        elif arr[mid]==1:
            mid+=1
        else:
            arr[mid],arr[high]=arr[high],arr[mid]
            high-=1
    return arr

arr=list(map(int, input("Enter array elements (0s, 1s, and 2s) separated by space: ").split()))

sorted_arr=sort(arr)

print("Sorted array:", sorted_arr)
