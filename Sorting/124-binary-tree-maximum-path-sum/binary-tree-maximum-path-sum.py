# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        
        max_sum = float('-inf')
        def getMaxsum(root):
            nonlocal max_sum
            if not root:
                return 0
            
            left_sum = max(getMaxsum(root.left), 0)
            right_sum = max(getMaxsum(root.right), 0)
            
            max_sum = max(max_sum, root.val + left_sum + right_sum)
            return max(left_sum, right_sum) + root.val
            
        getMaxsum(root)
        return max_sum