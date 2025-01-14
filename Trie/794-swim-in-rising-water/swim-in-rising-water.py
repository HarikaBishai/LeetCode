class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        dir = [(1,0),(-1,0),(0,1),(0,-1)]

        N = len(grid)

        h = [(grid[0][0],0,0)]
        visited = set()
        visited.add((0,0))

        while h:
            t, r, c = heapq.heappop(h)

            if r == N-1 and c == N-1:
                return t
            
            for i, j in dir:
                new_r = r + i
                new_c = c + j

                if new_r in range(N) and new_c in range(N) and  (new_r, new_c) not in visited:
                    heapq.heappush(h, (max(t, grid[new_r][new_c]), new_r, new_c))
                    visited.add((new_r, new_c))