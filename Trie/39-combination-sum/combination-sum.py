class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        

        stk = []
        out = []
        def getCombinations(i, sum, elements=[]):
            if sum == 0:
                out.append(elements[:])
                return

            if sum < 0 or i <= 0:
                return 
            if candidates[i-1] > sum:
                getCombinations(i-1, sum, elements)
            else:
                getCombinations(i-1, sum, elements)
                getCombinations(i, sum-candidates[i-1], elements + [candidates[i-1]])
            return
            
        getCombinations(len(candidates), target)
        return out