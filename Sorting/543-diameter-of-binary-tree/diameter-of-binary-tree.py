# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = 0
        def getDiameter(node):
            nonlocal maxDiameter
            if not node:
                return 0
            
            lheight = getDiameter(node.left)
            rheight = getDiameter(node.right)

            maxDiameter = max(maxDiameter, lheight + rheight)
            return max(lheight,rheight) + 1
        
        getDiameter(root)
        return maxDiameter