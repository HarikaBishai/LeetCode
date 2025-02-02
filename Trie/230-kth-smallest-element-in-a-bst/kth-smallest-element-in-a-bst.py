# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def inorder(node):
            
            nonlocal k
            print(k)
            if  node:
                
                
                leftVal = inorder(node.left)
                if leftVal: 
                    return leftVal
                k-=1
                if k == 0:
                    return node.val
                rightVal = inorder(node.right)
                if rightVal : return rightVal
            return 0
        
        return inorder(root)
            