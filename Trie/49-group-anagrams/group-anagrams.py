class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        out = defaultdict(list)

        for word in strs:
            sorted_word = "".join(sorted(word))
            out[sorted_word].append(word)

        return list(out.values())