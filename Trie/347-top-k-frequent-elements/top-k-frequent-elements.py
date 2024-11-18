import heapq as h
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        counter = Counter(nums)

        largest = [key for key, val in h.nlargest(k, counter.items(), key=lambda x: x[1])]
       
        return largest
        