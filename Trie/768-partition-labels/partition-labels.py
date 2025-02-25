class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {c: i for i, c in enumerate(s)}

        start,end = 0, 0
        ans = []

        for r, c in enumerate(s):
            end = max(end, last[c])
            if end == r:
                ans.append(r-start+1)
                start= r+1
        return ans