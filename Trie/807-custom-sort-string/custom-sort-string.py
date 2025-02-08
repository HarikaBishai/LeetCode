class Solution:
    def customSortString(self, order: str, s: str) -> str:
        

        map = { c: i for i,c in enumerate(order)}
        s = list(s)
        s.sort(key=lambda x: map.get(x, len(s))) 
        return "".join(s)

        