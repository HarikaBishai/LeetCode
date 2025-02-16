class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        

        unique_sequences = set()
        out = set()
        l = 0
        curr_seq = deque()
        for i in range(len(s)):
            curr_seq.append(s[i])

            if i >= 10:
                curr_seq.popleft()
            
            if len(curr_seq) == 10:
                seq = "".join(curr_seq)
                if seq in unique_sequences:
                    out.add(seq)
                else:
                    unique_sequences.add(seq)
        return list(out)


            
