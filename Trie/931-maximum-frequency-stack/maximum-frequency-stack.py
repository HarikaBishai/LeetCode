class FreqStack:

    def __init__(self):
        self.stk = {}
        self.count = 0
        self.counter = {}

    def push(self, val: int) -> None:
        if val not in self.counter:
            self.counter[val] = 1
        else:
            self.counter[val] += 1
        
        if self.counter[val] not in self.stk:
            self.stk[self.counter[val]] = []
        self.stk[self.counter[val]].append(val)
        self.count = max(self.count, self.counter[val])
    def pop(self) -> int:
        if not self.stk:
            return -1
        else:
            ele = self.stk[self.count].pop()
            if not self.stk[self.count]:
                del self.stk[self.count]
                self.count-=1
            self.counter[ele]-=1
            if self.counter[ele] == 0:
                del self.counter[ele]
            return ele


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()