# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.ans = True

        def calculateHeight(node):
            if not node:
                return 0
            left = calculateHeight(node.left)
            right = calculateHeight(node.right)
            if abs(left - right) > 1:
                self.ans = False
            return 1 + max(left, right)
        calculateHeight(root)
        return self.ans