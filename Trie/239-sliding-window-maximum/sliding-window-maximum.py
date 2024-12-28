class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        out = []
        for i in range(len(nums)):
            while q and  q[-1][1] < nums[i]:
                q.pop()

            q.append((i, nums[i]))
 

            if i >= k-1:
                out.append(q[0][1])
            
            if q and q[0][0] <= i-k+1:
                q.popleft()
        
        return out


