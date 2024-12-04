class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        

        curr_sum = 0
        minLen = float('inf')
        prefixSumHeap = [(0,-1)]

        for i, n in enumerate(nums):
            curr_sum += n

            while prefixSumHeap and curr_sum - prefixSumHeap[0][0] >= k:
                prefix, idx= heapq.heappop(prefixSumHeap)

                minLen = min(minLen, i-idx)


            heapq.heappush(prefixSumHeap, (curr_sum, i))

        return -1 if minLen == float('inf') else minLen