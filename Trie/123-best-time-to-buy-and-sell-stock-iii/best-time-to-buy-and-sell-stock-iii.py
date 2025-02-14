class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        leftProfit = [0]*n
        rightProfit = [0]*n

        minPrice = float('inf')
        for i in range(1,n):
            minPrice = min(prices[i-1], minPrice)
            leftProfit[i] = max(leftProfit[i-1], prices[i] - minPrice)

            
        maxPrice = float('-inf')
        for i in range(n-2, -1, -1):
            maxPrice = max(prices[i+1], maxPrice)
            rightProfit[i] = max(rightProfit[i+1], maxPrice - prices[i])


        maxProfit = 0
        for i in range(1, n):
            maxProfit = max(maxProfit, leftProfit[i] + rightProfit[i])
        
        return maxProfit