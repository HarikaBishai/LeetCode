class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        

        n = len(board)

        cells = {}

        columns = [ i for i in range(n) ]
        label = 1
        for i in range(n-1, -1, -1):
            for col in columns:
                cells[label] = (i, col)
                label+=1
            columns.reverse()


        q = deque([1])
        seen = set([1])
        target = n**2
        moves = 0
        while q:
            for _ in range(len(q)):
                pos = q.popleft()
                if pos == target:
                    return moves
                for i in range(1, 7):
                    new_pos = pos + i
                    if new_pos <= n**2:
                        r,c = cells[new_pos]

                        new_pos = new_pos if board[r][c] == -1 else board[r][c]

                        if new_pos not in seen:
                            q.append(new_pos)
                            seen.add(new_pos)
            moves = moves+1

        return -1


