class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if not prices:
            return 0
        profit = 0

        n = len(prices)

        max_val = prices[-1]
        for i in range(n-2, -1, -1):
            
            max_val = max(max_val, prices[i])
            profit = max(max_val-prices[i], profit)
        return profit