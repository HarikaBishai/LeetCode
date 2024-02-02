class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        l , r = 0, len(arr) - 1

        while(l<r):
            mid = (l + r)//2
            if arr[mid - 1] <= arr[mid] and arr[mid+1] <= arr[mid]:
                return mid
            elif arr[mid-1] > arr[mid]:
                r=mid 
            else:
                l=mid 
            