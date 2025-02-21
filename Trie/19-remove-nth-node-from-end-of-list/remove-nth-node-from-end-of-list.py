# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        

        if not head:
            return head

        slow = head
        fast = head
        while fast and n:
            fast = fast.next
            n-=1
        prev = None

        while slow and fast:
            prev = slow
            slow = slow.next
            fast = fast.next
       
        if slow == head:
            return head.next
        else:
            prev.next = slow.next
        return head