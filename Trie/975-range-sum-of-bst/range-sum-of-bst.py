# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        sum = 0
        def dfs(root):
            nonlocal sum
            if not root:
                return
            if low <= root.val <= high:
                sum+= root.val
                dfs(root.left)
                dfs(root.right)
            elif root.val < low:
                dfs(root.right)
            elif root.val > high:
                dfs(root.left)
            
        dfs(root)
        return sum