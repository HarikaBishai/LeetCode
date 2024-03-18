class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        


        l = 0
        out = []
        h = []
        for r in range(len(nums)):
            # print(h, -1*nums[l])
            heapq.heappush(h,(-nums[r], r))
            while h[0][1] <= r-k:
                heapq.heappop(h)

            if r >= k-1:
                out.append(-h[0][0])

        return out


