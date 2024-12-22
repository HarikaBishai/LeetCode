class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)

        maxLen = 0

        for num in nums:
            if num-1 in numsSet:
                continue
            
            currLen = 1
            while num + currLen  in numsSet:
                currLen+=1
                
            maxLen = max(maxLen, currLen)
        return maxLen
                