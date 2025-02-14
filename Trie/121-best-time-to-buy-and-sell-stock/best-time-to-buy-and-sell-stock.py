class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfVal = 0
        maxVal = 0
        for i in range(len(prices)-1, -1, -1):
            price = prices[i]
            maxVal = max(price, maxVal)
            maxProfVal = max(maxProfVal, maxVal-price)

        return maxProfVal

