# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        maxLength = 0
        def dfs(node, prev):
            nonlocal maxLength
            if not node:
                return 0
            
            leftMax = dfs(node.left, "left")
            rightMax = dfs(node.right, "right")

            maxLength = max(maxLength, max(leftMax, rightMax))

            if not prev:
                return maxLength
            elif prev == 'left':
                return 1 + rightMax
            else:
                return 1 + leftMax
        dfs(root, "")
        return maxLength            