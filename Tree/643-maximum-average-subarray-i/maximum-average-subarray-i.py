class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        

        curr_sum = sum(nums[:k])
        out = curr_sum/k
        l = 0
        for i in range(k, len(nums)):
            curr_sum = curr_sum - nums[l] + nums[i]
            out = max(out, curr_sum/k)
            l+=1
        return out