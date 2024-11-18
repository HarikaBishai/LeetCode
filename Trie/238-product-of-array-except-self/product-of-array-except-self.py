class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        out = [1]*n

        l = [1]*n
        r = [1]*n

        for i in range(1,n):
            l[i] = nums[i-1]*l[i-1]
        for i in range(n-2, -1, -1):
            r[i] = nums[i+1]*r[i+1]
        for i in range(n):
            out[i] = l[i]*r[i]
        return out