# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        def reverse(node):
            curr = node
            prev = None

            while curr:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            return prev
        

        fast, slow = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        end = reverse(slow)
        curr = head
        while curr and curr.next!=end:
            curr_next, end_next= curr.next, end.next
            curr.next = end
            end.next = curr_next
            curr, end = curr_next, end_next
           
        
        return head
            