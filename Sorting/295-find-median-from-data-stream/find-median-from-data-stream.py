class MedianFinder:

    def __init__(self):
        self.a = []
        self.b = []
        

    def addNum(self, num: int) -> None:
        if not self.a:
            heapq.heappush(self.a, -num)
            return
        

        if len(self.a) == len(self.b):
            if self.b[0] < num:
                ele = heapq.heappushpop(self.b, num)
                heapq.heappush(self.a, -ele)
            else:
                heapq.heappush(self.a, -num)
        else:
            if -self.a[0] > num:
                ele = heapq.heappushpop(self.a, -num)
                heapq.heappush(self.b, -ele)
            else:
                heapq.heappush(self.b, num)



    def findMedian(self) -> float:
        if len(self.a) == len(self.b):
            return (-self.a[0] + self.b[0])/2
        else:
            return -self.a[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()