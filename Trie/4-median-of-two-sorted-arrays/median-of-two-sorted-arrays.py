class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        n1 = len(nums1)
        n2 = len(nums2)
        total = n1+n2 
        half = (total) // 2


        l = 0
        r = n1 - 1
        while True:
            i = (l+r)//2
            j = half - i - 2

            aLeft = nums1[i] if i >= 0 else float('-inf')
            aRight = nums1[i+1] if i+1 < n1 else float('inf')
            bLeft = nums2[j] if j >= 0 else float('-inf')
            bRight = nums2[j+1] if j+1 < n2 else float('inf')

            if aLeft <= bRight and bLeft <= aRight:
                if total % 2:
                    return min(aRight, bRight)
                return (min(aRight, bRight) + max(aLeft , bLeft)) / 2
            elif aLeft > bRight:
                r = i-1
            else:
                l = i+1

