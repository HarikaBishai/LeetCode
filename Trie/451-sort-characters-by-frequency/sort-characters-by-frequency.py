import heapq 
class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)

        h = []

        for key, val in counter.items():
            heapq.heappush(h,(-val, key))

        out = ''

        while h:
            val, key = heapq.heappop(h)
            out += - val * key
        return out