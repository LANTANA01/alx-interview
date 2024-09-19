#!/usr/bin/python3
"""
Main file for testing
"""

def makeChange(coins, total):
    # Initialize dp array with large values (except dp[0])
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # Check if the total can be met
    if dp[total] == float('inf'):
        return -1
    else:
        return dp[total]
