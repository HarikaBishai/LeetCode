class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        out = []
        for i in range(n-2):
            l = i+1

            r = n-1
            if nums[i] > 0:
                break
            if i > 0:
                if nums[i-1] == nums[i]:
                    continue

            while l < r:
                curr_sum = nums[i] + nums[l] + nums[r]
                if curr_sum == 0:
                    out.append((nums[i],nums[l],nums[r]))
                    l+=1
                    r-=1
                    while nums[l-1] == nums[l] and l<r:
                        l+=1
                elif curr_sum < 0:
                    l+=1
                else:
                    r-=1
        return out