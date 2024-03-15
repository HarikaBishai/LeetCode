class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """


        # zipped = map(lambda x : list(x)[::-1],  list(zip(*matrix)))
        # print(list(zipped))

     
        # for i in range(m):
        #     matrix[i][:] = matrix[i][::-1]
        # return list(zipped)
        
        n = len(matrix)
        for i in range(n):
            for j in range(i+1 ,n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(n):
            matrix[i][:] = matrix[i][::-1]
        return matrix