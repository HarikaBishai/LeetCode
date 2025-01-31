# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        p_nodes = []
        q_nodes = []

        def dfs(root, node, path):
            path.append(root)
            if root == node:
                return True
            
            if root.left:
                if dfs(root.left, node, path):
                    return True
            if root.right:
                if dfs(root.right, node, path):
                    return True
            

            path.pop()
            return False
        dfs(root, p, p_nodes)
        dfs(root, q, q_nodes)


        minLen = min(len(p_nodes), len(q_nodes))

        for i in range(minLen-1, -1, -1):
            if p_nodes[i] == q_nodes[i]:
                return p_nodes[i]
        


        
            

