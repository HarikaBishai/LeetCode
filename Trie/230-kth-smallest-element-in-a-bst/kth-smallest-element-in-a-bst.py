# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        out = 0
        def inorder(root):
            nonlocal out, k
            if root:
                inorder(root.left)
                print(root)
                k-=1
                if k == 0:
                    out = root.val
                    return
                inorder(root.right)
        inorder(root)
        return out