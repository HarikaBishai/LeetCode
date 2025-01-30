# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        out = []
        q = deque()
        q.append(root)

        while q:

            curr_out = []
            for _ in range(len(q)):
                node = q.popleft()

                curr_out.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            out.append(curr_out)
        return out
