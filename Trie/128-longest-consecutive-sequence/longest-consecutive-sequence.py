class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)

        out = 0
        for num in nums:
            if num - 1 not in num_set:
                count = 1
                curr = num
                while curr+1 in num_set:
                    curr+=1
                    count+=1
                out = max(count, out)

           
        return out
            
