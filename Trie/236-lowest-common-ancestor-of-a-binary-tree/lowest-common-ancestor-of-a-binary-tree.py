# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def getpath(self, root, node, path=[]):
        if not root:
            return False
        path.append(root)
        if root == node:
            return True

        if root.left: 
            if self.getpath(root.left, node, path):
                return True
        if root.right:
            if self.getpath(root.right, node, path):
                return True
        path.pop()
        return False

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if not root:
            return None

        pathp = []
        pathq = []
        self.getpath(root, p, pathp)
        self.getpath(root, q, pathq)

        minlen = min(len(pathp), len(pathq))

        lastMatched= None

        for i in range(minlen):
            if pathq[i] != pathp[i]:
                return lastMatched
            lastMatched = pathp[i]
        return lastMatched
            



        