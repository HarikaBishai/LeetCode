class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)

        maxHeap = [-1*x for x in counter.values()]
        heapq.heapify(maxHeap)

        q = deque()

        time = 0

        while maxHeap or q:
            time+=1
            if maxHeap:
                cnt = heapq.heappop(maxHeap)
                if cnt+1 != 0:
                    q.append((cnt+1, time+n))
            
            if q:
                if q[0][1] == time:
                    heapq.heappush(maxHeap,q.popleft()[0])
        return time
