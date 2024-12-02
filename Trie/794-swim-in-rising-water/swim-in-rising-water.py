class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        N = len(grid)


        visited = set([(0,0)])
        h = [(grid[0][0],0,0)]

        while h:
            elevation, r,c = heapq.heappop(h)

            if r == N-1 and c== N-1:
                return elevation

            directions = [(-1,0),(1,0),(0,1),(0,-1)]

            for i , j in directions:
                new_r = r+i
                new_c = c+j
                if new_r in range(N) and new_c in range(N) and (new_r, new_c) not in visited:
                    heapq.heappush(h,(max(elevation, grid[new_r][new_c]), new_r, new_c))
                    visited.add((new_r, new_c))
        return -1
