class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        countObj = Counter(nums)
        
        nums = list(set(sorted(nums)))
        
        earn1 , earn2 = 0, 0
        
        for i in range(len(nums)):
            currEarn = nums[i] * countObj[nums[i]]
            temp = earn2
            if i > 0 and nums[i-1] + 1 == nums[i]:
                earn2 = max(earn2, currEarn + earn1)
            else:
                earn2 = earn2 + currEarn
            earn1 = temp
        return earn2