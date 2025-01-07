# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        s = []

        def dfs(root):
            
            if not root:
                return
            s.append(str(root.val))
            if root.left or root.right:
                s.append('(')
                dfs(root.left)
                s.append(')')
                if root.right:
                    s.append('(')
                    dfs(root.right)
                    s.append(')')
        dfs(root)
        s = "".join(s)
        return s