from collections import defaultdict
class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        
        for edge in paths:
            s, e = edge
            graph[s].append(e)
            graph[e].append(s)
            
        
        ans = [0]*n
        
        for garden in range(1, n+1):
            used_colors =[ans[i-1] for i in  graph[garden]]
            
            
            for color in range(1, 5):
                if color not in used_colors:
                    ans[garden-1] = color
                    break
        return ans