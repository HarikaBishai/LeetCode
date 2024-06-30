class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        h = []
        i = 0
        for key, value in counter.items():
            if i < k:
                heapq.heappush(h,(value, key))
            else:
                # if h[0][0] < value:
                heapq.heappushpop(h,(value, key))
            i+=1 
        out = []
        while h:
            out.append(heapq.heappop(h)[1])

        return out