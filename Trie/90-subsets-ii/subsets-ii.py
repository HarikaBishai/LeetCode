class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        stk = []
        out = []
        nums.sort()
        def dfs(i):

            out.append(stk.copy())

            for j in range(i,len(nums)):
                if j != i and nums[j] == nums[j-1]:
                    continue
                stk.append(nums[j])
                
                dfs(j+1)

                stk.pop()
                
                    
        dfs(0)
        return out