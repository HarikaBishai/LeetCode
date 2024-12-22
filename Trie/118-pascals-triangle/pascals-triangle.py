class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        out = []

        for i in range(numRows):
            curr = [1]*(i+1)

            if i > 1:
                for j in range(1, i):
                    curr[j] = out[-1][j-1] + out[-1][j]
                
            out.append(curr)

        return out