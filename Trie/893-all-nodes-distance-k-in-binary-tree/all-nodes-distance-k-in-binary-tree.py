# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        

        def addParent(curr, parent):
            if curr:
                curr.parent = parent
                addParent(curr.left, curr)
                addParent(curr.right, curr)

        addParent(root, None)

        out = []
        visited = set()
        def dfs(node, dis):
            if not node or node in visited:
                return
            visited.add(node)
            if dis == 0:
                out.append(node.val)
                return 
            
            dfs(node.left, dis-1)
            dfs(node.right, dis-1)
            dfs(node.parent, dis-1)

        
        dfs(target, k)
        return out

