# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        


        def _isValid(root, low=float('-inf'), high=float('inf')):
            if not root:
                return True
            
            if low < root.val < high:
                return _isValid(root.left, low, root.val) and _isValid(root.right, root.val , high)
            
            return False
        
        return _isValid(root)