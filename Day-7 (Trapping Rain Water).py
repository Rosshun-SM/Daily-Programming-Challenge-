# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 22:10:59 2024

@author: Rosshun
"""
def trap(heights):
    if not heights or len(heights) < 3:     # Check if heights are valid
        return 0
    
    left, right = 0, len(heights) - 1       # Initialize pointers and max height trackers
    max_left, max_right = heights[left], heights[right]
    trapped_water = 0
    
    while left < right:
        if heights[left] <= heights[right]:
            if heights[left] >= max_left:
                max_left = heights[left]
            else:
                trapped_water += max_left - heights[left]
            left += 1
        else:
            if heights[right] >= max_right:
                max_right = heights[right]
            else:
                trapped_water += max_right - heights[right]
            right -= 1
    
    return trapped_water


arr = eval(input("Input: height[] = "))
print("Ouput: ",trap(arr))