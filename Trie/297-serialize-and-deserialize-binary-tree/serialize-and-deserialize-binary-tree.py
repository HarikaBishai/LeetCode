# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        result = []
        
        def dfs(root):
            if not root:
                result.append("N")
                return 
            result.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        print(result)
        return ",".join(result)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        

        if not data:
            return None
        preorder = data.split(",")
        i = 0
        def dfs():
            nonlocal i
            if preorder[i] == "N":
                i+=1
                return None
            
            root = TreeNode(int(preorder[i]))
            i+=1
            root.left = dfs()
            root.right = dfs()
            return root
        return dfs()


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))