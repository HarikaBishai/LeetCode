# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        
        rep = defaultdict(int)
        out = []
        def tarverse(root):
            if not root:
                return ""
            curr_repr = '(' + tarverse(root.left) + ')' + str(root.val) + '(' + tarverse(root.right) + ')'

            rep[curr_repr] += 1
            if rep[curr_repr] == 2:
                out.append(root)
            return curr_repr
        
        tarverse(root)
        return out