class StockSpanner:

    def __init__(self):
        self.stk = []

    def next(self, price: int) -> int:
        span = 1
        while self.stk and self.stk[-1][0] <= price:
            currPrice, currSpan = self.stk.pop()
            span+=currSpan
        
        self.stk.append((price, span))
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)