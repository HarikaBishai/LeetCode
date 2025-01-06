# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        def reverse(l1):
            prev, next = None, None

            curr = l1
            while curr:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            return prev
        

        def getMid():
            slow, fast = head, head

            while slow and fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            
            return slow

        midPtr = getMid()
        reveseHalf = reverse(midPtr)


        curr = head

        while  reveseHalf:
            if curr.val != reveseHalf.val:
                return False
            curr = curr.next
            reveseHalf = reveseHalf.next
        return True
