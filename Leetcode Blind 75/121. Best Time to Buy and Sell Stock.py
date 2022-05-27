# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # edge case: no profit if we do not sell stock
        if len(prices) == 0: return 0 

        profit = 0
        minStock = prices[0]
        for i in range(1, len(prices)):
            minStock = min(minStock, prices[i])
            profit = max(profit, prices[i] - minStock)
        return profit if profit > 0 else 0