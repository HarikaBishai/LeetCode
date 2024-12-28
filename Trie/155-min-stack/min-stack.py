class MinStack:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, val: int) -> None:
        if self.s1:
            top = self.s2[-1]
            if top > val:
                self.s2.append(val)
            else:
                self.s2.append(top)
            self.s1.append(val)
        else:
            self.s1.append(val)
            self.s2.append(val)
        

    def pop(self) -> None:
        if self.s1:
            self.s2.pop()
            return self.s1.pop()
        return None

    def top(self) -> int:
        if self.s1:
            return self.s1[-1]
        return None

    def getMin(self) -> int:
        if self.s2:
            return self.s2[-1]
        return None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()