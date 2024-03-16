class FileReader:
    def __init__(self, filePath) -> None:
        self.file = open(filePath, 'r')
        self.buf4 = ['']*4
        self.i4 = 0
        self.n4 = 0
        self.buf = []

    def read4(self, buf4):
        i = 0
        while i<4:
            char = self.file.read(1)
            if not char:
                break
            buf4[i] = char
            i+=1
        return i
    
    def read(self, n):
        self.buf = []
        i = 0
        while i < n:
            if self.i4 < self.n4:
                self.buf.append(self.buf4[self.i4])
                self.i4+=1
                i+=1
            else:
                self.n4 = self.read4(self.buf4)
                if self.n4 == 0:
                    break
                self.i4 = 0
          
        return self.buf
    
    def close(self):
        self.file.close()

def main():
    file_reader = FileReader('./text')
    read_queries = [1,2,4,5]
    for i in range(len(read_queries)): 
        print(file_reader.read(read_queries[i]))
    
    file_reader.close()

if __name__ == '__main__':
    main()