class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        

        def canShip(cap):
            curr_w = 0
            n_days = 1
            for w in weights:
                curr_w += w
                if curr_w > cap:
                    n_days+=1
                    curr_w = w
            return n_days <= days
        

        l = max(weights)
        r = sum(weights)
        ans = -1
        while l<=r:
            m = (l+r)//2

            if canShip(m):
                ans = m
                r =m-1
            else:
                l = m+1
        return ans

        