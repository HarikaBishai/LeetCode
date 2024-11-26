class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
    
        return heapq.nlargest(k, nums)[-1]
        h = nums
        heapq.heapify(h)

        while len(h)>k:
            heapq.heappop(h)

        return h[0]