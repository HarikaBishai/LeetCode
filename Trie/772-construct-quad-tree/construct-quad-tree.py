"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        

        def _construct(n, r, c):
            all_same = True

            for i in range(n):
                for j in range(n):
                    if grid[r][c] != grid[r+i][c+j]:
                        all_same = False
                        break
            if all_same:
                return Node(grid[r][c], True)

            n = n//2

            topLeft =  _construct(n, r, c)
            topRight = _construct(n, r , c+n)
            bottomLeft = _construct(n, r+n, c)
            bottomright = _construct(n, r+n, c+n)

            if topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomright.isLeaf and topLeft.val == topRight.val ==  bottomLeft.val == bottomright.val:
                return Node(topLeft.val, True)
            return Node(0, False, topLeft, topRight, bottomLeft, bottomright)

        return _construct(len(grid), 0, 0)


