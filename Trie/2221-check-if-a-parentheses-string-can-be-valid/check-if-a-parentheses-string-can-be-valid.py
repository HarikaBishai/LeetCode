class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        
        if len(s) %2:
            return False
        unlocked = []
        open = []


        for i, c in enumerate(s):
            if locked[i] == '0':
                unlocked.append(i)
            elif c == '(':
                open.append(i)
            else:
                if open:
                    open.pop()
                elif unlocked:
                    unlocked.pop()
                else:
                    return False

        while open and unlocked and open[-1] < unlocked[-1]:
            open.pop()
            unlocked.pop()
        if open:
            return False
        return True