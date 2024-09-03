class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_el = max(piles)
        l = 1
        r = max_el

        def calculateTotalTime(n):
            time = 0
            for i in piles:
                time+=math.ceil(i/n)
            return time

        ans = max_el
        while l<=r:
            m = (l + r)//2
            total_time = calculateTotalTime(m)
            if total_time <= h:
                ans = min(ans, m)
                r=m-1
            else:
                l=m+1
            
        return ans