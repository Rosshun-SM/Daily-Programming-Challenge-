# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 15:00:33 2024

@author: Rosshun
"""
import math

def  LCM(n,m):
    return (abs(n * m) // math.gcd(n, m))


n = int(input("Input: N = "))
m = int(input("       M = "))
print("Output:", LCM(n,m))