# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 21:02:34 2024

@author: Rosshun
"""
def prime_fact(n):
    factors = []
    
    if n % 2 == 0:
        while n % 2 == 0:
            n //= 2
        factors.append(2)
    
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            factors.append(i)
            while n % i == 0:
                n //= i
    
    if n > 2:
        factors.append(n)
    return factors


n = int(input("Input: N = "))
print("Output:", prime_fact(n))