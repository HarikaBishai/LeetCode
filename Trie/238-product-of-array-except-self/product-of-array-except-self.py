class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if not n:
            return []
        out = [1]*n

        for i in range(1,n):
            out[i] = out[i-1] * nums[i-1]

        right = 1
        for i in range(n-2, -1, -1):
            right *= nums[i+1]
            out[i] = out[i]*right

        return out