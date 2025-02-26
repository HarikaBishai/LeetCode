class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        n = len(nums)
        for i in range(n-2):
            l = i+1
            r = n-1
            while l<r:
                sum = nums[i] + nums[l] + nums[r]
                if sum == 0:
                    res.add((nums[i], nums[l], nums[r] ))
                    l+=1
                    r-=1
                elif sum > 0:
                    r-=1
                else:
                    l+=1
        return list(res)
