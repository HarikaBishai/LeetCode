# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if not p:
            return q
        if not q:
            return p
        if p.val > q.val:
            p,q = q,p

        def _dfs(root):
            
            if root.val >= p.val and root.val <= q.val:
                return root
            elif root.left and p.val < root.val and q.val < root.val:
                return _dfs(root.left)
            elif root.right and p.val > root.val and q.val > root.val:
                return _dfs(root.right)
        return _dfs(root)