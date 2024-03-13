from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        pacific_queue = deque()
        atlantic_queue = deque()


        m  = len(heights)
        n  = len(heights[0])

        for i in range(m):
            pacific_queue.append((i, 0))
            atlantic_queue.append((i, n-1))

        for i in range(n):
            pacific_queue.append((0, i))
            atlantic_queue.append((m-1, i))
        
        def bfs(queue):
            rechable = set()
            while queue:
                curr = queue.popleft()
                r, c = curr
                rechable.add(curr)

                directions = [(-1,0), (0,1),(0,-1), (1,0)]

                for dir in directions:
                    new_r = r + dir[0]
                    new_c = c + dir[1]

                    if new_r < 0 or new_r >= m or new_c < 0 or new_c >= n:
                        continue
                    
                    if (new_r, new_c) in rechable:
                        continue
                    
                    if heights[new_r][new_c] < heights[r][c]:
                        continue
                    queue.append((new_r, new_c))
            return rechable

        pacific_reachable = bfs(pacific_queue)
        atlantic_reachable = bfs(atlantic_queue)



        return pacific_reachable.intersection(atlantic_reachable)

