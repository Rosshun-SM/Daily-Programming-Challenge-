# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 22:03:24 2024

@author: Rosshun
"""
def merge_sort_arr(arr1,arr2,m,n):
    for i in range(n-1,-1,-1):
        last=arr1[m-1]
        j=m-2

        while j>=0 and arr1[j]>arr2[i]:
            arr1[j+1]=arr1[j]
            j-=1

        if last>arr2[i]:
            arr1[j+1]=arr2[i]
            arr2[i]=last

print("Input:-")
arr1=eval(input("arr1: "))   #[4, 6, 10]
arr2=eval(input("arr2: "))   #[2, 3, 8]
merge_sort_arr(arr1,arr2,len(arr1),len(arr2))
print("\nOutput:-")
print("arr1:",arr1)
print("arr2:",arr2)