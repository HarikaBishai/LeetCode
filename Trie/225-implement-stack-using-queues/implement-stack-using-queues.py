class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)

        for i in range(len(self.q)-1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        if self.q:
            return self.q.popleft()
        return None

    def top(self) -> int:
        if self.q:
            return self.q[0]
        return None
    def empty(self) -> bool:
        return not self.q


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()