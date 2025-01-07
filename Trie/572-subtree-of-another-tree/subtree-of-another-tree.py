# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
  
        def isSub(root, subRoot):
            if isSame(root, subRoot):
                return True
            elif root.left and isSub(root.left, subRoot):
                return True
            elif root.right and isSub(root.right,subRoot):
                return True
            else:
                return False

        def isSame(p,q):
            if not p and not q:
                return True
            elif p and q:
                if p.val != q.val:
                    return False
                return isSame(p.left, q.left) and isSame(p.right, q.right)
            else:
                return False
        
        return isSub(root, subRoot)