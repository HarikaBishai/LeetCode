class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {c: i for i, c in enumerate(s)}

        j,l = 0, 0
        ans = []

        for r, c in enumerate(s):
            j = max(j, last[c])
            if j == r:
                ans.append(r-l+1)
                l= r+1
        return ans