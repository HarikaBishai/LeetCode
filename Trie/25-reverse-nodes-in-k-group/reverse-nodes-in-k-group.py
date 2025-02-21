# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        
        def get_length(head):
            i = 0
            curr = head
            while curr:
                curr = curr.next
                i+=1
            return i


        def _reverse(head):
            if get_length(head) < k:
                return head, None
            prev = None
            next = None
            curr = head
            i = 0
            while curr:
                if i == k :
                    break
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
                i+=1
            return prev, curr

        
        dummy = ListNode()
        dummy.next = head
        curr = dummy

        while curr.next:
           
            k_reversed, next = _reverse(curr.next)
            curr.next = k_reversed
            print(k_reversed)
            while curr.next:
                curr = curr.next
            curr.next = next
            

        return dummy.next