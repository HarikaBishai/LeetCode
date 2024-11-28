class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def isPalindrome(s):
            l, r = 0, len(s)-1
            while l<=r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True

        def dfs(s, partitions=[]):
            if not s:
                res.append(partitions)
                return
            for i in range(1, len(s)+1):
                if isPalindrome(s[:i]):
                    
                    dfs(s[i:], partitions + [s[:i]])
            

        dfs(s, [])
        return res


