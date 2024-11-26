# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def getString(root):
            if not root:
                return ""
            if not root.left and not root.right:
                return  str(root.val) 
            else:
                leftString = getString(root.left)
                rightString = getString(root.right)
                leftString =  "(" + leftString + ")"
                rightString = "" if not rightString else "(" + rightString + ")"

                return str(root.val) + leftString + rightString
            
        s = getString(root)
        return s