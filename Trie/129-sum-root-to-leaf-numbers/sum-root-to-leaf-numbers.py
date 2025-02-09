# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        
        out = 0
        def dfs(node, curr_s):
            nonlocal out
            if not node:
                return
            curr_s += str(node.val)

            if not node.left and not node.right:
                out += int(curr_s)
                return
            dfs(node.left, curr_s)
            dfs(node.right, curr_s)
        dfs(root, '')
        return out