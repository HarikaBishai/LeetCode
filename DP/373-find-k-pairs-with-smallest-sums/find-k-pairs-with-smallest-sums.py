class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        hp = []
        heapq.heapify(hp)
        for i in range(min(len(nums2), k)):
            heapq.heappush(hp, (nums1[0]+ nums2[i], nums1[0], nums2[i], 0))

        out = []
        i = 0
        while i<k:
            sum_val, n1, n2, idx = heapq.heappop(hp)
            out.append([n1,n2])
            if idx+1< len(nums1):
                heapq.heappush(hp, (nums1[idx+1]+n2,nums1[idx+1], n2, idx+1))
            i+=1
        return out