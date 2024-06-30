class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s).items()
        out = ''
        h = []
        for key, val in counter:
            heapq.heappush(h,(-val, key))

        while h:
            val, key =  heapq.heappop(h)
            out += key * (-val)

        return out
        
