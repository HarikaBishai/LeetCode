# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root: return []
        out = []
        q = deque([root])
        while q:
            maxElement = float('-inf')
            for i in range(len(q)):
                node = q.popleft()

                maxElement = max(maxElement, node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            out.append(maxElement)
        return out