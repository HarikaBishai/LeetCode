class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        prefix_sum = {0:1}
        out = 0
        curr_sum = 0
        for i in nums:
            curr_sum += i

            if curr_sum - k in prefix_sum:
                out+= prefix_sum[curr_sum - k]

            prefix_sum[curr_sum] = prefix_sum.get(curr_sum, 0) + 1

            
        
        return out


