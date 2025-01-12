class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        stk = []
        out = []
        nums.sort()
        def getSubSets(i):
            if i == len(nums):
                out.append(stk[:])
                return

            stk.append(nums[i])
            getSubSets(i+1)
            stk.pop()
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i = i + 1
            
            getSubSets(i+1)
        
        getSubSets(0)
        return out
