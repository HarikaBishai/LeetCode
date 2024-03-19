# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        if not root: return 0

        count = 0


        def getCount(root):
            nonlocal count
            if not root:
                return False
            
            count+=1

            getCount(root.left)
            getCount(root.right)

            return True

        getCount(root)
        return count