class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        out = set()

        n = len(nums)
        for i in range(n-2):
            l = i+1
            r = n-1
            while l < r:
                curr_sum = nums[i] + nums[l] + nums[r]

                if curr_sum == 0:
                    out.add((nums[i], nums[l], nums[r]))
                if curr_sum > 0:
                    r-=1
                else:
                    l+=1
        return list(out)