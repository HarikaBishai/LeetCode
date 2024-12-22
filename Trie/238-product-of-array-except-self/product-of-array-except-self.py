class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        out = [1]*n
        
        prefix = 1

        for i in range(1,n):
            prefix = prefix * nums[i-1]
            out[i] = prefix
            

        suffix = 1
        for i in range(n-1, -1, -1):
            out[i] *= suffix
            suffix *= nums[i]
        
        return out