class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.h = []
        

        for i in range(len(nums)):
            if i < k:
                heapq.heappush(self.h, nums[i])
            else:
                heapq.heappushpop(self.h, nums[i])

        
    def add(self, val: int) -> int:
        heapq.heappush(self.h,val)
        if len(self.h) > self.k:
            heapq.heappop(self.h)

        return self.h[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)