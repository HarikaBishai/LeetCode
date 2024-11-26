# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        maxSum = float('-inf')


        def getMaxSum(root):
            nonlocal maxSum
            if not root:
                return 0
            
            leftPathSum =  getMaxSum(root.left) 
            rightPathSum = getMaxSum(root.right)

            leftPathSum = 0  if leftPathSum < 0 else leftPathSum
            rightPathSum = 0 if rightPathSum < 0 else rightPathSum
            maxSum = max(maxSum, leftPathSum + rightPathSum + root.val)


            return max(root.val + leftPathSum, rightPathSum + root.val)
        getMaxSum(root)
        return maxSum
