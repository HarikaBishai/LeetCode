class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        

        topSum = sum(grid[0])
        bottom = 0
        res = float('inf')
        for i in range(len(grid[0])):
            topSum -=  grid[0][i]
            secondBot = max(topSum, bottom)
            res = min(res, secondBot)
            bottom += grid[1][i]
        return res

 

        prefixRow1 = grid[0].copy()
        prefixRow2 = grid[1].copy()


        for i in range(1,len(grid[0])):
            prefixRow1[i] += prefixRow1[i-1]
            prefixRow2[i] += prefixRow2[i-1]
        res = float('inf')

        
        for i in range(len(grid[0])):
            top = prefixRow1[-1] - prefixRow1[i]
            bottom = prefixRow2[i-1] if i > 0 else 0
            print(top, bottom)
            secondBot = max(top, bottom)

            res = min(res, secondBot)
        return res
