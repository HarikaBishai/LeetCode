# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        

        prev = None
        minDistance = float('inf')

        def _inorder(root):
            nonlocal minDistance, prev
            if root:
                _inorder(root.left)

                if prev:
                    minDistance = min(minDistance, abs(prev.val - root.val))
                
                prev = root

                _inorder(root.right)
        _inorder(root)
        return minDistance