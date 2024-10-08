# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 17:00:39 2024

@author: Rosshun
"""
def coin_change(coins, amount):
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != amount + 1 else -1


coins = eval(input("Input: coins = "))
amount = int(input("      amount = "))
print("Output:",coin_change(coins, amount))