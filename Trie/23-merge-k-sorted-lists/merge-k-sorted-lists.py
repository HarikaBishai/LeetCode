# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        

        def mergeLists(l1,l2):
            dummy = ListNode(0)
            curr = dummy

            while l1 or l2:
                if l1 and l2:
                    if l1.val <= l2.val:
                        curr.next = ListNode(l1.val)
                        l1 = l1.next
                    else:
                        curr.next = ListNode(l2.val)
                        l2 = l2.next
                elif l1:
                    curr.next = ListNode(l1.val)
                    l1 = l1.next
                else:
                    curr.next = ListNode(l2.val)
                    l2 = l2.next
                curr = curr.next

            return dummy.next
        out = lists
        i = 0
        while len(out) > 1:
            i = 0
            temp = []
            while i < len(out):
                l1 = out[i]
                l2 = None
                if i+1 < len(out):
                    l2 = out[i+1]
                
                temp.append(mergeLists(l1, l2))
                i= i+2
            out = temp
        return out[0] if out else None
                

