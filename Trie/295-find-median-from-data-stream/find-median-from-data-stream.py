class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        self.length = 0

    def addNum(self, num: int) -> None:
        if self.length%2:
            if -self.maxHeap[0] > num:
                popped = heapq.heapreplace(self.maxHeap, -num)
                heapq.heappush(self.minHeap, -popped)
            else:
                heapq.heappush(self.minHeap, num)

        else:

            
            if self.maxHeap and self.minHeap[0] < num:
                popped = heapq.heapreplace(self.minHeap, num)
                heapq.heappush(self.maxHeap, -popped)
            else:
                heapq.heappush(self.maxHeap, -num)

        self.length+=1
    def findMedian(self) -> float:
        if self.length%2:
            return -self.maxHeap[0]
        else:
            if self.length:
                return (-self.maxHeap[0] + self.minHeap[0])/2
            else:
                return float('-inf')


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()