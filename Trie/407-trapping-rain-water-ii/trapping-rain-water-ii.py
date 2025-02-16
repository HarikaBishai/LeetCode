class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        ROWS = len(heightMap)
        COLS = len(heightMap[0])

        boundary = []
        for i in range(ROWS):
            for j in range(COLS):
                if i == 0 or i == ROWS-1 or j == 0 or j == COLS-1:
                    heapq.heappush(boundary, (heightMap[i][j], i,j))
                    heightMap[i][j] = -1
        
        total_water = 0

        while boundary:
            minHeight, r, c = heapq.heappop(boundary)
            dir = [(-1,0),(1,0),(0,-1),(0,1)]
            for i, j in dir:
                nei_r = i + r
                nei_c = j + c
                if nei_r in range(ROWS) and nei_c in range(COLS) and heightMap[nei_r][nei_c]!=-1:
                    nei_h = heightMap[nei_r][nei_c]
                    if nei_h < minHeight:
                        total_water += minHeight - nei_h
                    
                    heapq.heappush(boundary, (max(minHeight, nei_h), nei_r, nei_c) )
                    heightMap[nei_r][nei_c] = -1
        return total_water
