class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        mapper = set()
        mapper.add(s[:10])
        out = set()
        for i in range(1, len(s)-9):
            if s[i:i+10] not in mapper:
                mapper.add(s[i:i+10])
            else:
                out.add(s[i:i+10])
        return list(out)