# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        length = mountainArr.length()
        l = 1
        r =  length-2

        peak = r

        while l <= r:

            m = (l+r)//2
            ele = mountainArr.get(m)
            prev = mountainArr.get(m-1)
            nextEle = mountainArr.get(m+1)
            if prev < ele and ele > nextEle:
                peak = m
                break
            elif prev < ele:
                l = m+1
            else:
                r = m-1
        
        print(peak, mountainArr.get(peak))
        l = 0
        r = peak

        while l<=r:
            m = (l+r)//2
            ele = mountainArr.get(m)

            if ele == target:
                return m
            elif ele < target:
                l = m+1
            else:
                r = m-1
            
        l = peak
        r = length-1
        while l<=r:
            m = (l+r)//2
            ele = mountainArr.get(m)
            if ele == target:
                return m
            elif ele < target:
                r = m-1
            else:
                l = m+1
        return -1

