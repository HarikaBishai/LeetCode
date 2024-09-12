class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        oneDArr = []

        for row in matrix:
            oneDArr += row
        
        l ,r = 0, len(oneDArr)-1

        while l<=r:
            m = (l+r)//2
            if oneDArr[m] == target:
                return True
            elif oneDArr[m] < target:
                l = m+1
            else:
                r = m-1
        return False