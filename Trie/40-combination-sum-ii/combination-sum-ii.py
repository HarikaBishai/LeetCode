class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        

        out = []

        candidates.sort()
        def getCombinations(sum, i, elements=[]):
            if sum == 0:
                out.append(elements[:])
                return
            
            if sum < 0 or i <= 0:
                return 
            
            if candidates[i-1] > sum:
                getCombinations(sum, i-1, elements)
            else:
                getCombinations(sum-candidates[i-1], i-1, elements + [candidates[i-1]])

                while i-2>=0 and candidates[i-1] == candidates[i-2]:
                    i=i-1
                getCombinations(sum, i-1, elements)


        getCombinations(target, len(candidates))
        return out
