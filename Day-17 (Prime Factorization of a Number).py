# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 21:02:34 2024

@author: Rosshun
"""
def prime_fact(n):
    factors = []
    
    while n % 2 == 0:
        n //= 2
        if 2 not in factors:  
            factors.append(2)
    
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            n //= i
            if i not in factors:  
                factors.append(i)
    
    if n > 2:
        factors.append(n)
        
    return factors

n = int(input("Input: N = "))
print("Output:", prime_fact(n))