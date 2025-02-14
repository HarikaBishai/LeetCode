class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        stk =[]
        counter = Counter(nums)
        out = []
        def dfs():

            if len(stk) == len(nums):
                out.append(stk.copy())

            for  num in counter:
                if counter[num] > 0:
                    counter[num]-=1
                    stk.append(num)
                    dfs()
                    stk.pop()
                    counter[num]+=1
                    

        dfs()
        return out