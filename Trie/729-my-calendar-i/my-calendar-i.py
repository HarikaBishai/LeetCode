class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None

class MyCalendar:

    def __init__(self):
        self.root = None
    
    def insert(self, node, startTime, endTime):

        if endTime <= node.start:
            if not node.left:
                node.left = Node(startTime, endTime)
                return True
            else:
                return self.insert(node.left, startTime, endTime)
        elif startTime >= node.end:
            if not node.right:
                node.right = Node(startTime, endTime)
                return True
            else:
                return self.insert(node.right, startTime, endTime)
        else:
            return False


    def book(self, startTime: int, endTime: int) -> bool:
        if not self.root:
            self.root = Node(startTime, endTime)
            return True
        
        return self.insert(self.root, startTime, endTime)


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)