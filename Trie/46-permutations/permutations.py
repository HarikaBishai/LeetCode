class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        


        # stk = []
        # out = []
        # def permutate(i):
        #     if i == len(nums):
        #         out.append(nums.copy())
        #         return

        #     for j in range(i,len(nums)):
        #         nums[i], nums[j] = nums[j],nums[i]
        #         permutate(i+1)
        #         nums[i], nums[j] = nums[j],nums[i]
        # permutate(0)
        # return out



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