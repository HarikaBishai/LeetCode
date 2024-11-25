# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast_ptr, slow_ptr = head , head

        while fast_ptr and fast_ptr.next:
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next

        
        def reverse(start):
            curr = start
            prev = None
            next = None
            while curr:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            return prev

        end = reverse(slow_ptr)
        

        start = head
        while end:
            if start.val == end.val:
                start= start.next
                end = end.next
            else:
                return False
        return True