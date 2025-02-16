class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        left = 0

        maxLen = 0
        
        minHeap = []
        maxHeap = []
        for r in range(len(nums)):
            heapq.heappush(minHeap, (nums[r], r))
            heapq.heappush(maxHeap, (-nums[r], r))

            while -maxHeap[0][0] - minHeap[0][0] > limit:
                left = min(minHeap[0][1], maxHeap[0][1]) + 1

                while minHeap[0][1] < left:
                    heapq.heappop(minHeap)
                while maxHeap[0][1] < left:
                    heapq.heappop(maxHeap)
            
            maxLen = max(maxLen, r - left + 1)

        return maxLen