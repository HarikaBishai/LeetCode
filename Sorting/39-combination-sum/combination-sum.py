class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        final_out = []
        def getCombinations(candidates, n, target, out=[]):
            print(target, out)
            if target == 0:
                if out:
                    final_out.append(out)
                return
                
            if target < 0 or n<0:
                return 
            getCombinations(candidates, n-1, target, out)
            getCombinations(candidates, n, target-candidates[n], out+[candidates[n]])
            
            return

        getCombinations(candidates, len(candidates)-1, target)
        return final_out