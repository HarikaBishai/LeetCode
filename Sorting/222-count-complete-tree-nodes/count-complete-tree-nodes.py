# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
            count=0
            visited = set()
            def dfs(node):
                nonlocal count
                if not node:
                    return 
                if node in visited:
                    return
                count+=1
                visited.add(node)
                if not node.left:
                    return
                dfs(node.left)
                dfs(node.right)
            dfs(root)
            return count
