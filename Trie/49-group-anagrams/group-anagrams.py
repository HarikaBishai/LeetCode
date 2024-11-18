class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)


        for s in strs:
            curr = "".join(sorted(s))
            groups[curr].append(s)

        return list(groups.values())
