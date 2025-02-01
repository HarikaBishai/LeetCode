"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        pathNodes = set()
        curr = p
        while curr:
            pathNodes.add(curr)
            curr = curr.parent

        print(pathNodes)
        while q and q not in pathNodes:
            q = q.parent
        return q

