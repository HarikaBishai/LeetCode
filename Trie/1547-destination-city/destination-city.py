class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        
        nodes = set()
        for u, v in paths:
            nodes.add(u)

        
        for u, v in paths:
            if v not in nodes:
                return v

        