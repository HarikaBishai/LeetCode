# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        def merge_tree(root1, root2):

            if not root1 and not root2:
                return None
            root = None
            if root1 and root2:
                root = TreeNode(root1.val +  root2.val)
                root.left = merge_tree(root1.left, root2.left)
                root.right = merge_tree(root1.right, root2.right)
            elif root1:
                root = root1
            else:
                root = root2

            return root
        return merge_tree(root1, root2)