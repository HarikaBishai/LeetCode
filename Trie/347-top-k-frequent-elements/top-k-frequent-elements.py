import heapq as h
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        if k == len(nums):
            return nums

        counter = Counter(nums)

        largest = []

        for key in counter:
            h.heappush(largest,(-counter[key], key))

        out = []

        for i in range(k):
            count, key = h.heappop(largest)
            out.append(key)
        return out
        