# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return None
        def mergeList(list1, list2):
           
            dummyNode = ListNode()
            out = dummyNode
            i = 0
            j = 0

            while list1 and list2:
                if list1.val <= list2.val:
                    out.next = list1
                    out = out.next
                    list1 = list1.next
                else:
                    out.next = list2
                    out = out.next
                    list2 = list2.next
            
            while list1:
                out.next = list1
                out = out.next
                list1 = list1.next
            
            while list2:
                out.next = list2
                out = out.next
                list2 = list2.next
            return dummyNode.next

        while len(lists) > 1:
            temp = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = None
                if i + 1 < len(lists):
                    list2 = lists[i+1]
                if list1 and list2:
                    temp.append(mergeList(list1, list2))
                elif list1:
                    temp.append(list1)
                else:
                    temp.append(list2)
            lists = temp
        return lists[0]


            




