import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [k for k,v in list(Counter(nums).most_common(k))]
        # count = list((Counter(nums)).items())
        # count = [(-1 * v, k) for k, v in count]
        # heapq.heapify(count)
        # out = []
        # for i in range(k):
        #     temp, ele =   heapq.heappop(count)
        #     out.append(ele)
        
        # return out