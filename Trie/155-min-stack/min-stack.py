class MinStack:

    def __init__(self):
        self.stk = []
        self.minStk = []
        

    def push(self, val: int) -> None:
        self.stk.append(val)
        if not self.minStk:
           self.minStk.append(val)
        else:
            top = self.minStk[-1]
            if top < val:
                self.minStk.append(top)
            else:
                self.minStk.append(val)

    def pop(self) -> None:
        if not self.stk:
            return None
        else:
            top = self.stk.pop()
            self.minStk.pop()
            return top

    def top(self) -> int:
        if not self.stk:
            return None
        else:
            return self.stk[-1]
        

    def getMin(self) -> int:
        
        if not self.stk:
            return None
        else:
            return self.minStk[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()