# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def build(preorder, inorder):
            if not preorder:
                return None
            
            node = TreeNode(preorder[0])
            index = inorder.index(preorder[0])

            node.left = build(preorder[1:index+1], inorder[:index])
            node.right = build(preorder[index+1:], inorder[index+1:])
            return node
        return build(preorder, inorder)