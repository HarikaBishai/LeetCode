class TicTacToe:

    def __init__(self, n: int):
        # self.board = [[0]*n for _ in range(n)]
        # self.n = n
        self.rows = [0]*n
        self.cols = [0]*n
        self.diag = 0
        self.anti_diag = 0
        self.n = n


    def move(self, row: int, col: int, player: int) -> int:
        n = self.n
        curr_value = 1 if player == 1 else -1

        self.rows[row] += curr_value
        self.cols[col] += curr_value

        if row == col:
            self.diag += curr_value
        
        if col == n - row -1:
            self.anti_diag += curr_value

        
        if abs(self.rows[row]) == n or abs(self.cols[col]) == n or abs(self.diag) == n or abs(self.anti_diag) == n:
            return player
        return 0


        # self.board[row][col] = player

        # def check_row():
        #     for i in range(self.n):
        #         if self.board[row][i]!= player:
        #             return False
        #     return True
        
        # def check_col():
        #     for i in range(self.n):
        #         if self.board[i][col]!= player:
        #             return False
        #     return True
        
        # def check_left_diag():
        #     for i in range(self.n):
        #         if self.board[i][i]!= player:
        #             return False
        #     return True
        
        # def check_right_diag():
        #     for i in range(self.n):
        #         if self.board[i][self.n-i-1]!= player:
        #             return False
        #     return True
        
        # return player if check_row() or check_col() or check_left_diag() or check_right_diag() else 0
        

        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)