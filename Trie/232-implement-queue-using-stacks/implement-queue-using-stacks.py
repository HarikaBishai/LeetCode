class MyQueue:

    def __init__(self):
        self.push_stk = []
        self.pop_stk = []

    def push(self, x: int) -> None:
        self.push_stk.append(x)

    def pop(self) -> int:
        if self.pop_stk:
            return self.pop_stk.pop()
        
        elif self.push_stk:
            for i in range(len( self.push_stk)):
                self.pop_stk.append(self.push_stk.pop())
            return self.pop_stk.pop()
        
        return None
        

    def peek(self) -> int:
        if self.pop_stk:
            return self.pop_stk[-1]
        elif self.push_stk:
            return self.push_stk[0]
        else:
            return None


    def empty(self) -> bool:
        if not self.pop_stk and not self.push_stk:
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()