# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 20:29:28 2024

@author: Rosshun
"""
import math

def count_divisors(n):
    div_count = 0
    
    for i in range(1, int(math.sqrt(n)) + 1):
        if n%i == 0:
            if i == n//i:  
                div_count += 1
            else:
                div_count += 2
    return div_count


n = int(input("Input: N = "))
print("Ouput:", count_divisors(n))