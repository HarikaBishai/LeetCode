"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(0)

        temp = head

        curr = dummy


        mapping = {}

        while temp:
            if temp in mapping:
                curr.next =  mapping[temp]
            else:
                curr.next =  Node(temp.val)
                mapping[temp] = curr.next
            curr = curr.next
            

            next = temp.next
            random = temp.random
            if random:
                if random in mapping:
                    curr.random =  mapping[random]
                else:
                    curr.random =  Node(random.val)
                    mapping[random] = curr.random
                
            temp = next
        return dummy.next






