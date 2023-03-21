#!/usr/bin/python3
"""Make Change.
"""


def makeChange(coins, total):
    """Determines the fewest number of coins needed to meet a given
    amount total when given a pile of coins of different values.
    """
    # Initialize a list to store the minimum number of coins
    # required for each value from 0 to total
    dp = [float('inf')] * (total + 1)

    # Base case: 0 coins are needed to make up a total of 0
    dp[0] = 0

    # Iterate over all possible values from 1 to total
    for i in range(1, total+1):
        # Try every coin in the list that is smaller than or
        # equal to the current value
        for j in range(len(coins)):
            if coins[j] <= i:
                # Compute the minimum number of coins required for
                # the current value
                # by taking the minimum of the number of coins required
                # for the current value
                # minus the value of the current coin, plus 1
                # (for the current coin itself)
                dp[i] = min(dp[i], dp[i-coins[j]] + 1)

    # If the final value in the dp table is still infinity, it means
    # the total cannot be made up by any number of coins
    if dp[total] == float('inf'):
        return -1
    else:
        return dp[total]
