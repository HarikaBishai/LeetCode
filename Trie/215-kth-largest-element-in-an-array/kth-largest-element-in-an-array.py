class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        return heapq.nlargest(k, nums)[-1]
        minHeap = []

        for i, n in enumerate(nums):
            if i < k:
                heapq.heappush(minHeap, n)
            elif minHeap[0] < n:
                heapq.heappushpop(minHeap, n)
        return minHeap[0]
