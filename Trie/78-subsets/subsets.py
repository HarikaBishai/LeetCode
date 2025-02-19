class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        


        stk = []
        out = []
        visited = set()
        def dfs(i):
            out.append(stk.copy())

           
            for j in range(i, len(nums)):
                stk.append(nums[j])
                dfs(j+1)
                stk.pop()
                
        
        dfs(0)
        return out