class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        plates = [i for i,val in enumerate(s) if val == '|']

        def get_lower_bound( target):
            l = 0 
            r = len(plates)-1
            ans = float('inf')
            while l<=r:
                m = (l+r)//2

                if plates[m] >= target:
                    ans = m
                    r = m-1
                else:
                    l = m+1
            return ans
        def get_upper_bound( target):
            ans = float('inf')
            l = 0 
            r = len(plates)-1
            while l<=r:
                m = (l+r)//2

                if plates[m] <= target:
                    ans = m
                    l = m+1
                else:
                    r = m-1
            return ans

        out = []
        for start , end in queries:
            left = get_lower_bound(start)
            right = get_upper_bound(end)
            print( left, right, start, end)
            if  left == float('inf') or right == float('inf') or right <= left  or abs(plates[left]-plates[right]) < 1:
                out.append(0)
            else:
                out.append(plates[right] - plates[left] - (right-left))

        return out

        