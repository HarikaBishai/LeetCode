# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(next=head)
        curr = head
        i = 0
        while i < n and curr:
            curr = curr.next
            i+=1
        
        
        start = dummy
        prev = None
        while curr:
            curr = curr.next
            start = start.next
        
        start.next = start.next.next
        return dummy.next


        