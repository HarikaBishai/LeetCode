# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    def __init__(self):
        self.buf4 = ['']*4
        self.i4 = 0
        self.n4 = 0
    def read(self, buf: List[str], n: int) -> int:
        
        i =  0
        while i < n:
            if self.i4 < self.n4:
                buf[i] = self.buf4[self.i4]
                self.i4+=1
                i+=1
            else:
                self.n4 = read4(self.buf4)
                if self.n4 == 0:
                    break
                self.i4 = 0
        return i