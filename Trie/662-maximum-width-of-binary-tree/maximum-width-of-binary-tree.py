# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque([[0, root]])
        maxWidth = 0
        while q:
            start = 0
            end = 0
            n = len(q)
            for i in range(n):
                num , node = q.popleft()
                if i == 0:
                    start = num
                if i == n-1:
                    end = num
                if node.left:
                    q.append([num*2, node.left])
                if node.right:
                    q.append([num*2+1 , node.right])
            maxWidth = max(maxWidth, end-start+1)
        return maxWidth
