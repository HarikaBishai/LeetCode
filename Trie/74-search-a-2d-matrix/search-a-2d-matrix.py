class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l ,r = 0, len(matrix)-1
        rowNo = -1
        while l <=r:
            mid = (l+r)//2
            if target >= matrix[mid][0] and target<=matrix[mid][-1]:
                rowNo = mid
                break
            if target < matrix[mid][0]:
                r = mid-1
            else:
                l = mid+1
        if rowNo == -1:  return False

        l, r = 0, len(matrix[rowNo])-1

        while l<=r:
            m = (l+r)//2
            if matrix[rowNo][m] == target:
                return True
            elif matrix[rowNo][m] < target:
                l=m+1
            else:
                r=m-1

        return False

