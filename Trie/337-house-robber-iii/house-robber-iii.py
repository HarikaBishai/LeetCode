# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        
        def dfs(node):

            if not node:
                return (0, 0)

            
            left = dfs(node.left)
            right = dfs(node.right)

            rob1 = node.val + left[1] + right[1]
            
            rob2 = max(left) + max(right)
            
            return [rob1, rob2]

        return max(dfs(root))


        return max(dfs(root,0,0))



