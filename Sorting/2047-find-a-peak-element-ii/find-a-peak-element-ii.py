class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:

        m = len(mat)
        n = len(mat[0])
        def getMaxRow(col):
            maxElement = -1
            index = -1
            for i in range(m):
                if mat[i][col] > maxElement:
                    maxElement =  mat[i][col]
                    index = i
            return index

     
        l = 0
        r = n-1
        while l<=r:
            mid = (l+r)//2
            row = getMaxRow(mid)
            left = mat[row][mid-1]  if mid>0 else -1
            right = mat[row][mid+1]  if mid<n-1 else -1

            if left < mat[row][mid] and right < mat[row][mid]:
                return (row, mid)
            elif left < mat[row][mid]:
                l = mid+1
            else:
                r= mid -1
        return (-1, -1)





        