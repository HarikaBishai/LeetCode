# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        levels = []
        q = deque([root])

        while q:
            level_sum = 0
            for _ in range(len(q)):
                node = q.popleft()
                level_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            levels.append(level_sum)
        

        q = deque([root])
        root.val = 0
        level = 1

        while q:
            
            for _ in range(len(q)):
                node = q.popleft()

                sibiling_val = (node.left.val if node.left else 0) + (node.right.val if node.right else 0)

                if node.left:
                    node.left.val = levels[level]-sibiling_val
                    q.append(node.left)
                if node.right:
                    node.right.val = levels[level]-sibiling_val
                    q.append(node.right)
            level+=1
        return root

