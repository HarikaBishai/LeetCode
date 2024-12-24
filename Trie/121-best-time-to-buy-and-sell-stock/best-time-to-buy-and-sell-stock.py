class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0


        stk = []

        for i, p in enumerate(prices):
            if i == 0:
                stk.append(p)
            else:
                while stk and stk[-1] >= p:
                    stk.pop()

                if len(stk):
                    maxP = max(maxP, p - stk[0])
                
                stk.append(p)
        return maxP