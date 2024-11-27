class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        curr = nums[:]
        out = []
        def dfs(curr, idx):
            if idx == len(curr):
                out.append(curr[:])
            for i in range(idx, len(curr)):
                curr[idx], curr[i] = curr[i], curr[idx]
                dfs(curr, idx+1)
                curr[idx], curr[i] = curr[i], curr[idx]

            # out.append(curr[:])
            
        dfs(curr,0)
        return out

            