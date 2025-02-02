class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        start = '0000'

        deadends = set(deadends)
        if start in deadends:
            return -1

        q = deque([start])
        seen = set([start])
        steps = 0
        while q:
            for _ in range(len(q)):
                seq = q.popleft()
                if seq == target:
                    return steps

                dir = [-1, 1]
                for i in range(4):
                    for j in dir:
                        digit = (int(seq[i]) + j) % 10
                        new_seq = seq[:i] + str(digit) + seq[i+1:]
                        if new_seq not in seen and new_seq not in deadends:
                            q.append(new_seq)
                            seen.add(new_seq)
            steps+=1
        return -1