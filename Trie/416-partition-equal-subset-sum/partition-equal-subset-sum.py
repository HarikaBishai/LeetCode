class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2:
            return False
        target = sum(nums)//2
        dp = set([0])
        for i in range(len(nums)-1, -1, -1):
            numSet = set()

            for j in dp:
                numSet.add(nums[i]+j)
                numSet.add(j)
            dp = numSet
            if target in numSet:
                return True
        

        return False