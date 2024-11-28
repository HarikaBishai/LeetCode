class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()


        res = []
        currSum = 0
        def getCombinations(target,path, n):
            if target == 0:
                res.append(path[:])
                return 
            
            if target <= 0 or n <= 0:
                return 
            
            if candidates[n-1] > target:
                getCombinations(target,path, n-1)
            
            else:
                path.append(candidates[n-1])
                getCombinations(target-candidates[n-1],path, n-1)
                path.pop()
                while n-1>0 and candidates[n-1] == candidates[n-2]:
                    n-=1
                getCombinations(target,path, n-1)
            

        getCombinations(target,[], len(candidates))

        return res
