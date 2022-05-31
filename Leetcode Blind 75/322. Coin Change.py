class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
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