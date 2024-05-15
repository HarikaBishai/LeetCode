class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array

        l1 ,l2 = 0, 0
        n =  len(nums1)  + len(nums2)
        print((n//2) + 1)
        merged = []
        i = 0
        while l1 < len(nums1) and l2 < len(nums2) and i < ((n//2)+1) :
            if nums1[l1] < nums2[l2]:
                merged.append(nums1[l1])
                l1+=1
            else:
                merged.append(nums2[l2])
                l2+=1
            i+=1
        
        while l1 < len(nums1) and i < ((n//2)+1):
            merged.append(nums1[l1])
            i+=1
            l1+=1
        
        while l2 < len(nums2) and i < ((n//2)+1):
            merged.append(nums2[l2])
            i+=1
            l2+=1
        
        if n%2 == 1:
            return merged[-1]
        else:
            return (merged[-1] + merged[-2])/2
