# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def mergeTwoLists(list1, list2):
            dummy = ListNode(0)
            tail = dummy

            while  list1 and list2:
                if list1.val <= list2.val:
                    tail.next = list1
                    list1 = list1.next
                else:
                    tail.next = list2
                    list2 = list2.next
                tail = tail.next
            
            while list1:
                tail.next = list1
                list1 = list1.next
                tail = tail.next
            
            while list2:
                tail.next = list2
                list2 = list2.next
                tail = tail.next

            return dummy.next



        

        while len(lists) > 1:
            listgroups = [lists[i:i+2] for i in range(0, len(lists), 2)]
            temp = []
            for i in range(len(listgroups)):
                if len(listgroups[i]) > 1:
                    temp.append(mergeTwoLists(*listgroups[i]))
                else:
                    temp.append(listgroups[i][0])
            lists = temp
        return lists[0] if lists else None


