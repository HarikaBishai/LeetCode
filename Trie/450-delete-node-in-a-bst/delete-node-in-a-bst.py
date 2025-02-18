# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        


        def _deleteNode(root):
            if not root:
                return None
            if root.val == key:
                if not root.left and not root.right:
                    root = None
                    print(root)
                elif not root.left:
                    root = root.right
                elif not root.right:
                    root = root.left
                else:
                    curr = root.right
                    while curr.left:
                        curr = curr.left
                    root.val ,curr.val = curr.val, root.val
                    root.right = _deleteNode(root.right)
            elif root.val < key:
                root.right = _deleteNode(root.right)
            else:
                root.left = _deleteNode(root.left)
            return root
        root = _deleteNode(root)
        return root