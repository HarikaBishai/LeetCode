class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        if self.maxHeap and self.maxHeap[0] < num:
            heapq.heappush(self.maxHeap, num)
        else:
            heapq.heappush(self.minHeap, -num)

        if len(self.minHeap) > len(self.maxHeap) + 1 :
            val = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -val)
        elif len(self.maxHeap) > len(self.minHeap) + 1:
            val = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, val)

        
        
        

    def findMedian(self) -> float:

        
        if len(self.minHeap) > len(self.maxHeap):
            return -self.minHeap[0]
        elif len(self.maxHeap) > len(self.minHeap):
            return self.maxHeap[0]
        
        return (-self.minHeap[0] + self.maxHeap[0])/2
            


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()