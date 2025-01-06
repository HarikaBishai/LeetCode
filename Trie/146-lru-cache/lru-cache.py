class ListNode:
    def __init__(self,val=0, key=0):
        self.val = val
        self.next = None
        self.prev = None
        self.key = key

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.left = ListNode()
        self.right= ListNode()
        self.left.next = self.right
        self.right.prev = self.left
        self.hash = {}


    def remove(self,node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev

    def insertAtRight(self,node):
        prev,next = self.right.prev, self.right
        prev.next = node
        next.prev = node
        node.prev = prev
        node.next = next
        
    def get(self, key: int) -> int:
        if key in self.hash:
            self.remove(self.hash[key])
            self.insertAtRight(self.hash[key])
            return self.hash[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hash:
            self.remove(self.hash[key])

        node = ListNode(value,key)
        self.insertAtRight(node)
        self.hash[key] = node

        if len(self.hash) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.hash[lru.key]


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)