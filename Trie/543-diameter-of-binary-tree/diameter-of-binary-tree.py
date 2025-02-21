# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        


        maxDiameter = 0

        def get_max_diameter(root):
            nonlocal maxDiameter
            if not root:
                return 0
            
            leftHeight = get_max_diameter(root.left)
            rightHeight = get_max_diameter(root.right)

            maxDiameter = max(maxDiameter, leftHeight + rightHeight)
            return 1 + max(leftHeight, rightHeight)
        get_max_diameter(root)

        return maxDiameter
            