# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        

        maxSum = float('-inf')
        def pathSum(node):
            nonlocal maxSum
            if node == None:
                return 0

            left_sum = max(pathSum(node.left), 0)
            right_sum = max(pathSum(node.right), 0)
            maxSum = max(maxSum, 
                left_sum + node.val + right_sum
                
            )
            return max(left_sum+node.val, right_sum+node.val )

        pathSum(root)
        return maxSum