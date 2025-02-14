# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.stack = []
        self.left_inorder(root)

    def left_inorder(self, root):
        while root:
            self.stack.append(root)
            root = root.left
    def next(self) -> int:
        if not self.stack:
            return -1
        topNode = self.stack.pop()

        if topNode.right:
            self.left_inorder(topNode.right)
        return topNode.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()