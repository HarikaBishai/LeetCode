# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        
        graph = defaultdict(list)
        def build_graph(root, parent):
            if root and parent:
                graph[root.val].append(parent.val)
                graph[parent.val].append(root.val)
        
            if root.left:
                build_graph(root.left, root)
            if root.right:
                build_graph(root.right, root)

        build_graph(root, None)

        q = deque([start])
        visited = set([start])
        time = -1

        print(graph)
        while q:

            for i in range(len(q)):
                node = q.popleft()

                for nei in graph[node]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append(nei)
            time+=1
        return time