class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        out = []
        ROWS = len(mat)
        COLS = len(mat[0])

        r, c = 0, 0
        dir = False
        
        while True:
            out.append(mat[r][c])
            if r == ROWS-1 and c == COLS-1:
                break

            if dir == True:

                if c-1 < 0 or r+1 == ROWS:
                    dir = False
                    print(r, c, r+1, ROWS)
                    if r + 1 == ROWS:
                        c = c + 1
                    else:
                        r = r + 1
                else:
                    r = r+1
                    c = c-1
            elif dir == False:
                if r - 1 < 0 or  c + 1 == COLS:
                    dir = True
                    if c + 1 == COLS:
                        r = r+1
                    else:
                        c = c + 1
                else:
                    r = r-1
                    c = c+1


        return out