class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        result = []
        left = 0
        up = 0
        right = COLS-1
        down = ROWS-1
        while len(result) < ROWS * COLS:
            for i in range(left, right+1):
                result.append(matrix[up][i])
            
            for i in range(up+1, down+1):
                result.append(matrix[i][right])
            
            if up!=down:
                for col in range(right-1, left-1, -1):
                    result.append(matrix[down][col])
            
            if left!=right:
                for row in range(down-1, up, -1):
                    result.append(matrix[row][left])
            
            up+=1
            right-=1
            down-=1
            left+=1
        
        return result