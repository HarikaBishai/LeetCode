class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        

        ROWS = len(matrix)
        COLS = len(matrix[0])

        zero_rows = set()
        zero_cols = set()

        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)

        for row in zero_rows:
            for j in range(COLS):
                matrix[row][j] = 0
        

        for col in zero_cols:
            for i in range(ROWS):
                matrix[i][col] = 0
        

        