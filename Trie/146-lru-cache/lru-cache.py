class Node:
    def __init__(self, val=0, key=0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:


    def __init__(self, capacity: int):
        self.capacity = capacity
        self.left = Node()
        self.right = Node()
        self.left.next = self.right
        self.right.prev = self.left
        self.hash = {}

    
    def insert(self, node):

        prev = self.right.prev
        next = self.right

        prev.next = node
        node.prev = prev
        node.next = next
        next.prev = node

        return node

        
    def remove(self, node):
        next = node.next
        prev = node.prev
        next.prev = prev
        prev.next = next

        


    def get(self, key: int) -> int:
        if key in self.hash:
            node = self.hash[key]
            self.remove(node)
            self.insert(node)
            self.hash[key] = node
            return node.val
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:

        new_node = Node(value, key)
        if key in self.hash:
            curr_node = self.hash[key]
            self.remove(curr_node)
            
            self.insert(new_node)
            self.hash[key] = new_node
        else:
            if len(self.hash) + 1 > self.capacity:
                left_node = self.left.next
                self.remove(left_node)
                del self.hash[left_node.key]
                self.insert(new_node)
                self.hash[key] = new_node
            else:
                self.insert(new_node)
                self.hash[key] = new_node


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)