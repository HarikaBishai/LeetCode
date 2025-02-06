# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        columnMapping = defaultdict(list)

        q = deque([(root, 0)])

        while q:
            node, column = q.popleft()
            columnMapping[column].append(node.val)
            if node.left:
                q.append((node.left, column-1))
            if node.right:
                q.append((node.right, column+1))
        
        return [columnMapping[i] for i in sorted(columnMapping.keys())]