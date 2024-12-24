class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0


        minBuy = prices[0]

        for p in prices:
            if p < minBuy:
                minBuy = p
            maxP = max(maxP, p - minBuy)
        return maxP