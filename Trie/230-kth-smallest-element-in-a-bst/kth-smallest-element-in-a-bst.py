# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        stk = []
        curr = root
        while curr or stk:
            while curr:
                stk.append(curr)
                curr = curr.left
            
            ele = stk.pop()
            count+=1
            if count == k:
                return ele.val

            curr = ele.right
        

                