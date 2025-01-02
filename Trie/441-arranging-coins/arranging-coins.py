class Solution:
    def arrangeCoins(self, n: int) -> int:
        l = 0

        r = n
        ans = 0
        while l<=r:
            m = (l+r)//2

            total = (m * (m+1)) // 2
            
            if n >= total:
                ans = max(m, ans)
                l = m+1
            else:
                r = m-1
        return ans
        