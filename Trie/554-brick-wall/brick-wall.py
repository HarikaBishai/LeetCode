class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        ROWS = len(wall)
        gaps = defaultdict(int)

        maxGaps = 0
        for r in range(ROWS):
            edge = 0
            for i in range(len(wall[r])-1):
                edge += wall[r][i]
                gaps[edge]+=1
                maxGaps = max(maxGaps, gaps[edge])
        return ROWS - maxGaps