class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out = []

        stk = []
        def getSubset(i,nums):
            if i == len(nums):
                out.append(stk[:])
                return 
            stk.append(nums[i])
            getSubset(i+1, nums)
            stk.pop()
            getSubset(i+1, nums)

        getSubset(0,nums)

        return out