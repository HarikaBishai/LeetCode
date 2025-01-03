class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        
        l = max(weights)
        r = sum(weights)


        def canShip(cap):
            day = 1
            currCap = cap
            for w in weights:
                if currCap - w < 0:
                    day+=1
                    currCap = cap
                currCap -=w 
                    
            
            return day <= days
            

        ans = r
        while l<=r:
            m = (l+r)//2
            if canShip(m):
                ans = min(m, ans)
                r=m-1
            else:
                l=m+1
        return ans