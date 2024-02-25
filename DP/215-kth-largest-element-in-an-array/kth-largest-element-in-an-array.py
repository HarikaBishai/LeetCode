import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
    
        nums = list(map(lambda x: -1 * x, nums))
        heapq.heapify(nums)
        out = -1 * nums[0]
        for i in range(k):
            out =-1 * heapq.heappop(nums)

        
        return out


        

        