# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:

        cnt = defaultdict(int)
        out = []
        def traverse(node):
            if not node:
                return ""
            
            rep = ( "(" + traverse(node.left) + ")"  + str(node.val) + "(" + traverse(node.right) + ")")

            cnt[rep]+=1

            if cnt[rep] == 2:
                out.append(node)
            return rep

        traverse(root)

        return out
