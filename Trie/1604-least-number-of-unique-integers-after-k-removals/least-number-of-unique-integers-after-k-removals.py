class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = Counter(arr)

        minHeap = [(count,key) for key, count in counter.items()]
        heapq.heapify(minHeap)
        print(minHeap)
        while minHeap and minHeap[0][0] <= k:
            count, val = heapq.heappop(minHeap)
            k -= count

        return len(minHeap) 