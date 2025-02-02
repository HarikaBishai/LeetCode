"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node

        rootNode = Node(node.val)
        visited = {}
        def dfs(clonedNode, originalNode):

            print(clonedNode.val)
            
            visited[originalNode] = clonedNode
            if originalNode.neighbors:
                for nei in originalNode.neighbors:

                    if nei in visited and clonedNode not in visited[nei].neighbors :
                        visited[nei].neighbors.append(clonedNode)

                    if nei not in visited:
                        # 
                        neiNode = Node(nei.val)
                        
                        dfs(neiNode, nei)
                        neiNode.neighbors.append(clonedNode)
                        # clonedNode.neighbors.append(neiNode)
            
                            
                   
        

        dfs(rootNode, node)
        

        return rootNode
        


