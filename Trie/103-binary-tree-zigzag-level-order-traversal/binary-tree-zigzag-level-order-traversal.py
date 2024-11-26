# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        q = deque()

        q.append(root)
        out = []
        level = 0
        while q:
            currNodes = deque()
            for _ in range(len(q)):
                curr = q.popleft()
               
                if level%2 == 0:
                    currNodes.appendleft(curr.val)
                else:
                    currNodes.append(curr.val)
                if curr.right:
                    q.append(curr.right)
                if curr.left:
                    q.append(curr.left)
                
            level+=1
            out.append(list(currNodes))
        return out
                    
