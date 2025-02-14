class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        minPrice = prices[0]

        maxProVal = 0

        for i in range(1,len(prices)):
            
            minPrice = min(prices[i], minPrice)
            maxProVal = max(maxProVal, prices[i] -  minPrice)
        return maxProVal