class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) <= k:
            return list(set(nums))
        counter = defaultdict(int)
        for i in nums:
            counter[i]+=1
        
        hp = []
        for i,key in enumerate(list(counter.keys())):
            if i < k:
                heapq.heappush(hp, (counter[key], key))
            elif hp[0][0] <= counter[key]:
                heapq.heapreplace(hp, (counter[key], key))
        out = []
        for count, val in hp:
            out.append(val)
        return out