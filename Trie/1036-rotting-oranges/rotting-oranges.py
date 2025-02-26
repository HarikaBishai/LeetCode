class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh_orange_count = 0
        time_lapse = 0
        rows, cols = len(grid), len(grid[0])
        directions = ((-1, 0), (0,-1), (1,0), (0,1))
        queue = collections.deque()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append([row, col])
                elif grid[row][col] == 1:
                    fresh_orange_count += 1
        if not fresh_orange_count:
            return 0
        time = 1
        while queue:
            for i in range(len(queue)):
                curr_row, curr_col = queue.popleft()

                for direction in directions:
                    new_row = curr_row + direction[0]
                    new_col = curr_col + direction[1]

                    if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] == 1:
                        grid[new_row][new_col] = 2
                        queue.append([new_row, new_col])
                        fresh_orange_count -= 1
                        if fresh_orange_count == 0:
                            return time
            time+=1
        if fresh_orange_count != 0:
            return -1

        return time_lapse


        