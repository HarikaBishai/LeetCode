# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root: return []
        q = deque()
        q.append(root)
        out = []
        while q:
            currLen = len(q)
            for i in range(currLen):
                curr = q.popleft()
                if i == currLen-1:
                   out.append(curr.val) 
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
        
        return out