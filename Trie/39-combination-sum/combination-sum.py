class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        out = []
        def getCombinations(target,n, path):
            if target == 0:
                out.append(path)
                return
            if target < 0 or n<=0:
                return 
            
            if candidates[n-1] > target:
                getCombinations(target,n-1, path)
            
            else:
                getCombinations(target,n-1, path)
                getCombinations(target-candidates[n-1],n, path + [candidates[n-1]])
        
        getCombinations(target,len(candidates), [])
        return out
                