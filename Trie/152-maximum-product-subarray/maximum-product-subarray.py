class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = float('-inf')
        n = len(nums)
        pref = 1
        suff = 1

        for i in range(n):
            if pref == 0:
                pref = 1
            if suff == 0:
                suff = 1
            
            pref = pref*nums[i]
            suff = suff*nums[n-i-1]
            ans = max(ans, pref, suff)
        return ans