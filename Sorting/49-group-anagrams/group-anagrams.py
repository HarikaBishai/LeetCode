class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        obj = defaultdict(list)

        for str in strs:
            curr_sorted = ''.join(sorted(str))
            obj[curr_sorted].append(str)
        
        return list(obj.values())