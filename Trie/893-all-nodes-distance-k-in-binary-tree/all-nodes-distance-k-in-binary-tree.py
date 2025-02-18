# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)

        def build_graph(node, parent):
            if node and parent:
                graph[node].append(parent)
                graph[parent].append(node)
            if node.left:
                build_graph(node.left, node)
            if node.right:
                build_graph(node.right, node)
            
        
        build_graph(root, None)
        
        level = 0

        q = deque([target])
        visited = set([target])
        out = []
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if level == k:
                    out.append(node.val)
                for nei in graph[node]:
                    if nei not in visited:
                        q.append(nei)
                        visited.add(nei)
                
            if level == k:
                break
            level+=1
        return out

