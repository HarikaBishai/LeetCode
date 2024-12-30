class FreqStack:

    def __init__(self):
        self.groups = defaultdict(list)
        self.counter = defaultdict(int)
        self.max = 0
    def push(self, val: int) -> None:
        self.counter[val] +=1
        self.groups[self.counter[val]].append(val)
        if self.max < self.counter[val]:
            self.max = self.counter[val]
    def pop(self) -> int:
        ele = self.groups[self.max].pop()

        if not self.groups[self.max]:
            self.max -= 1
        self.counter[ele]-=1
        return ele



# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()