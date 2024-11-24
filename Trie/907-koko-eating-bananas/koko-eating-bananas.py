class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l = 1
        r = max(piles)

        def canEat(k):
            count = 0

            for pile in piles:
                count+= math.ceil(float(pile)/k)
            
            return count
    

        while l<=r:
            mid = (l+r)//2
            hrs = int(canEat(mid))
            if hrs <=h:
                r = mid-1
            else:
                l = mid+1
        return l