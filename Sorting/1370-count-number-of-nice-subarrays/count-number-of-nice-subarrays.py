class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        curr_sum = 0
        sub_arrays = 0
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1

        for i in range(len(nums)):
            curr_sum += nums[i] % 2
            if curr_sum - k in prefix_sum:
                sub_arrays   += prefix_sum[curr_sum - k]
            prefix_sum[curr_sum] += 1
        return sub_arrays