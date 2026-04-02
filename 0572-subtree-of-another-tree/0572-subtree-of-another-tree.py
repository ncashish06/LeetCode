# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #Serialize both trees using preorder traversal (with null markers) into strings.
    def serialize(self, root):
        hash = []
        def dfs(node):
            if not node:
                hash.append("-#")
                return
            hash.append("-" + str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ''.join(hash)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        hashRoot = self.serialize(root)
        hashSubRoot = self.serialize(subRoot)
        return hashSubRoot in hashRoot