import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
    
        # nums = list(map(lambda x: -1 * x, nums))
        heapq.heapify(nums)
        out = nums[-1]
        for i in range(len(nums)-k + 1):
            out =heapq.heappop(nums)

        
        return out


        

        