# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def height(root):
            if not root:
                return 0
            
            leftHeight = height(root.left)
            rightHeight = height(root.right)

            return 1+ max(leftHeight, rightHeight)
        
        def check_balance(root):
            if not root:
                return True
            leftHeight = height(root.left)
            rightHeight = height(root.right)

            if abs(leftHeight - rightHeight) > 1:
                return False
            return check_balance(root.left) and check_balance(root.right)
        
        return check_balance(root)
            