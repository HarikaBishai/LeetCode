class FreqStack:

    def __init__(self):
        self.count = defaultdict(int)
        self.maxCount = 0
        self.stacks= defaultdict(list) 
    def push(self, val: int) -> None:
        self.count[val]+=1
        if self.count[val] > self.maxCount:
            self.maxCount+=1
        self.stacks[self.count[val]].append(val)

    def pop(self) -> int:
        if not self.maxCount:
            return null
        val = self.stacks[self.maxCount].pop()
        if not self.stacks[self.maxCount]:
            del self.stacks[self.maxCount]
            self.maxCount-=1
        self.count[val]-=1
        return val

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()