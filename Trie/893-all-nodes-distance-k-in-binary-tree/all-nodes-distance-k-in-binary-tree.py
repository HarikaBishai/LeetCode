# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        

        graph = defaultdict(list)
        def buildgraph(node, parent):
            if node and parent:
                graph[node.val].append(parent.val)
                graph[parent.val].append(node.val)
            if node.left:
                buildgraph(node.left, node)
            if node.right:
                buildgraph(node.right, node)

        buildgraph(root, None)

        visited = set([target.val])
        out = []
        def dfs(node, dist):

            if dist == k:
                out.append(node)
                return 
            
            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei, dist+1)
            

        dfs(target.val, 0)

        return out

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

