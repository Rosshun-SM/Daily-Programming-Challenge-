# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 21:20:41 2024

@author: Rosshun
"""
def fibonacci(n):
    if n == 0:
        return 0
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]


n = int(input("Input: "))
print("Ouput:", fibonacci(n))