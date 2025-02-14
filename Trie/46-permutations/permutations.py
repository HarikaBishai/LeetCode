class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        

        stk = []
        out = []
        path = set()
        def dfs():
            if len(stk) == len(nums):
                out.append(stk.copy())

            for num in nums:
                if num not in path:
                    path.add(num)
                    stk.append(num)
                    dfs()
                    stk.pop()
                    path.remove(num)
        dfs()
        return out