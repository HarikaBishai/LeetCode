class TicTacToe:

    def __init__(self, n: int):
        self.board = [[0]*n for _ in range(n)]
        self.n = n


        

    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = player

        def check_row():
            for i in range(self.n):
                if self.board[row][i]!= player:
                    return False
            return True
        
        def check_col():
            for i in range(self.n):
                if self.board[i][col]!= player:
                    return False
            return True
        
        def check_left_diag():
            for i in range(self.n):
                if self.board[i][i]!= player:
                    return False
            return True
        
        def check_right_diag():
            for i in range(self.n):
                if self.board[i][self.n-i-1]!= player:
                    return False
            return True
        
        return player if check_row() or check_col() or check_left_diag() or check_right_diag() else 0
        

        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)