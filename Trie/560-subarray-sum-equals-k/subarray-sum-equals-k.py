class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = defaultdict(int)
        res = 0
        curr_sum = 0
        prefix_sum[0]=1
        for n in nums:
            curr_sum += n
            if curr_sum - k in prefix_sum:
                res += prefix_sum[curr_sum - k]
            prefix_sum[curr_sum] += 1

        return res