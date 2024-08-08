class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:

        ver1 = list(map(int, version1.split('.')))
        ver2 = list(map(int, version2.split('.')))

        m = len(ver1)
        n = len(ver2)

        i = 0
        out = 0
        while i<n and i<m:
            if ver1[i] == ver2[i]:
                i+=1
                continue
            
            if ver1[i] < ver2[i]:
                return -1
            else:
                return 1
        while i < m:
            if ver1[i]:
                return 1
            i+=1
        
        while i < n:
            if ver2[i]:
                return -1
            i+=1
        return 0
        