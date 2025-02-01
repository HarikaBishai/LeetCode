# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = float('-inf')

        def dfs(root):
            nonlocal maxSum
            if not root:
                return 0

            leftSum = max(dfs(root.left), 0)
            rightSum = max(dfs(root.right), 0)


            maxSum = max(maxSum, leftSum + rightSum + root.val)

            return root.val + max(leftSum, rightSum)
        dfs(root)
        return maxSum