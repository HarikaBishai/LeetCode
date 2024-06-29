class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = nums[:k]
        heapq.heapify(h)

        for num in nums[k:]:
            if h[0] < num:
                heapq.heappushpop(h, num)
            
        
        return h[0]