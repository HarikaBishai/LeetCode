class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m*k :
            return -1
        def possible(day):
            cnt = 0
            noOfB = 0
            for i in bloomDay:
                if i <= day:
                    cnt+=1
                else:
                    noOfB += cnt // k
                    cnt = 0
            noOfB += cnt // k
            return noOfB >= m

        
        l = min(bloomDay)
        r = max(bloomDay)
        # ans = float('inf')
        while l<=r:
            mid = (l+r)//2
            if possible(mid):
                r=mid-1
            else:
                l=mid+1
        return l