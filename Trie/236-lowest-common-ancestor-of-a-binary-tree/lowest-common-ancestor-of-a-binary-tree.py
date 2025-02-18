# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        parent_mapping = {root: None}

        def dfs(root):
            if not root:
                return
            if root.left:
                parent_mapping[root.left] = root
                dfs(root.left)
            if root.right:
                parent_mapping[root.right] = root
                dfs(root.right)
        
        dfs(root)

        path_nodes = set()

        curr = p
        while curr:
            path_nodes.add(curr)
            curr = parent_mapping[curr]
        
        while q and q not in path_nodes:
            q = parent_mapping[q]
        return q