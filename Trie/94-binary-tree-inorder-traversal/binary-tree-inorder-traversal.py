# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stk = []
        curr = root
        while curr or stk:
            while curr:
                stk.append(curr)
                curr = curr.left
                
            curr = stk.pop()
            result.append(curr.val)
            curr = curr.right
        return result
        def inorder(node):
            if node:
                inorder(node.left)
                result.append(node.val)
                inorder(node.right)
        inorder(root)
        return result