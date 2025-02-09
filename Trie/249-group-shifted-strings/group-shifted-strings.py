class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        def getHash(s):

            key = []

            for i in range(1, len(s)):
                a = s[i-1]
                b = s[i]
                key.append(chr((ord(b)-ord(a))%26 + ord('a')))
            
            return "".join(key)

        key_mapping = defaultdict(list)

        for s in strings:
            hash_key = getHash(s)
            key_mapping[hash_key].append(s)
        return list(key_mapping.values())