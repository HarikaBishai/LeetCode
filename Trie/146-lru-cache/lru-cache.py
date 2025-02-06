class Node:
    def __init__(self,val = 0, key = 0):
        self.val = val
        self.prev = None
        self.next = None
        self.key = key

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash = {}
        self.left = Node()
        self.right = Node()
        self.left.next, self.right.prev = self.right, self.left


    def pop(self, node):
        nodePrev = node.prev
        nodeNext = node.next
        nodePrev.next = nodeNext
        nodeNext.prev = nodePrev
        return node.key

    def insert(self, node):
        prev = self.right.prev
        next = self.right.prev.next
        node.next = self.right
        node.prev = prev
        prev.next = node
        self.right.prev = node

    def get(self, key: int) -> int:
        # print(self.hash)
        if key in self.hash:
            self.pop(self.hash[key])
            self.insert(self.hash[key])
            return self.hash[key].val
        return -1




    def put(self, key: int, value: int) -> None:
        if key in self.hash:
            self.pop(self.hash[key])
            node = Node(value, key)
            self.insert(node)
            self.hash[key] = node
        else:
            node = Node(value, key)
            self.insert(node)
            self.hash[key] = node
        print(len(self.hash) ,self.capacity)
        if len(self.hash) > self.capacity:
            leftKey = self.pop(self.left.next)
            print(leftKey)
            if leftKey in self.hash:
                del self.hash[leftKey]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)