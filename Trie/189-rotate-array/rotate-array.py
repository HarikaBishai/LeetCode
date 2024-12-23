class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)<=1:
            return 
        n = len(nums)
        k = k%(n)
        def reverse(nums, l, r):
            while l<r:
                nums[l], nums[r] = nums[r], nums[l]
                l+=1
                r-=1
        reverse(nums,0, n-1)
        reverse(nums, 0, k-1)
        reverse(nums, k, n-1)



