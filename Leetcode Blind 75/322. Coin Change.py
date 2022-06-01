from typing import List, Tuple, Dict, TextIO

class Solution:
    def coinChange(coins: List[int], amount: int) -> int:
        
        # Solution 1: DP
        # edge case
        if amount == 0: return 0
        # dp[x] = min coin needed for a combination of x 
        # Ex: amount = 5, dp = [0, inf, inf, inf, inf, inf]
        dp = [float('inf')] * (1+amount) 
        dp[0] = 0
        # print(dp)

        for a in range(1, amount+1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], dp[a-c]+1)
        return dp[amount] if dp[amount] !=  float('inf') else -1

    
# Testing code
print(Solution.coinChange([2,3,5,7], 27)) # Output: 5
print(Solution.coinChange([2,3,5,7], 99)) # Output: 15
print(Solution.coinChange([2,3,5,7], 171)) # Output: 25
print(Solution.coinChange([2,3,5,7], 1028)) # Output: 148
print(Solution.coinChange([2,3,5,7], 10086)) # Output: 1442