class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0

        for num in nums_set:
            
            if num - 1 not in nums_set:
                curr = num
                j = 1
                while curr+1 in nums_set:
                    j+=1
                    curr+=1
                longest = max(longest, j)
        return longest


