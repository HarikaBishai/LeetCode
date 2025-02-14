# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getMid(self, head):
        slow = head
        fast = head
        slowPrev = None
        while fast and fast.next:
            slowPrev = slow
            fast = fast.next.next
            slow = slow.next
        
        if slowPrev:
            slowPrev.next = None
        
        return slow


    def merge(self, list1, list2):
        dummy = ListNode(0)

        curr = dummy
        while list1 or list2:
            if list1 and list2:
                if list1.val < list2.val:
                    curr.next = list1
                    list1 = list1.next
                else:
                    curr.next = list2
                    list2 = list2.next
            elif list1 :
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        
        return dummy.next
        
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head
        mid = self.getMid(head)

        left = self.sortList(head)
        right = self.sortList(mid)

        return self.merge(left, right)



