class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)


        len_buckets = [[] for i in range(len(nums))]

        for key, val in counter.items():
            len_buckets[val-1].append(key)

        out = []
        for i in range(len(nums)-1, -1, -1):
            for num in len_buckets[i]:
                out.append(num)
                if len(out) == k:
                    return out
