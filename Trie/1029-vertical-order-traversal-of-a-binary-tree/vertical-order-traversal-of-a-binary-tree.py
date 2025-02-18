# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        columnTable = defaultdict(dict)
        if not root:
            return []
        q = deque([(root, 0)])


        level = 0
        while q:
            for i in range(len(q)):
                node, column = q.popleft()
                if level in columnTable[column]:
                    columnTable[column][level].append(node.val)
                else:
                    columnTable[column][level] = [node.val]
                if node.left:
                    q.append((node.left, column-1))
                if node.right:
                    q.append((node.right, column+1))
            level+=1
        out = []
        for key in sorted(columnTable.keys()):
            curr = []
            for row in sorted(columnTable[key].keys()):
                curr += sorted(columnTable[key][row])
            out.append(curr)
        return out