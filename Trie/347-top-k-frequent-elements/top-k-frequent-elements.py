import heapq as h
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        counter = Counter(nums)

        largest = []
        for key, val in counter.items():        
            h.heappush(largest, (val, key))
            if k < len(largest):
                h.heappop(largest)



        
    
        out = [key for val, key in largest]
        return out
        