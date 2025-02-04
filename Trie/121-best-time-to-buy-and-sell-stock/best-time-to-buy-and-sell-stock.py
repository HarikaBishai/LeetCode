class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        maxValtoRight = prices[-1]

        maxProfit = 0

        for i in range(n-1, -1, -1):
            maxValtoRight = max(maxValtoRight, prices[i])
            maxProfit = max(maxValtoRight-prices[i], maxProfit)
        return maxProfit
