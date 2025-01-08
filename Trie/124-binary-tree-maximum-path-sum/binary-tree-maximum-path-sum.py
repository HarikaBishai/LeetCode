# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        sum = float('-inf')

        def pathSum(root):
            nonlocal sum
            if not root:
                return 0

            
            leftPathSum = max(pathSum(root.left), 0)
            RightPathSum = max(pathSum(root.right), 0)

            sum = max(sum, leftPathSum + RightPathSum + root.val)
            return root.val + max(leftPathSum, RightPathSum)
        pathSum(root)
        return sum