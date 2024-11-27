import heapq as h
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        counter = Counter(nums)

        buckets = [[] for i in range(len(nums)+1)]
        for key, val in counter.items():
            buckets[val].append(key)
        out = []
        for i in range(len(nums), 0, -1):
            for ele in buckets[i]:
                out.append(ele)
                if len(out) == k:
                    return out
        return out
        