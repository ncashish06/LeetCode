# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #At each node, calculate: maxLeft: max gain from the left subtree (0 if negative)
    #maxRight: max gain from the right subtree (0 if negative). The local max path passing through current node is: curr.val + maxLeft + maxRight
    #Update the global max sum (maxSumPath) with the local max.
    #Return the max gain to the parent node: curr.val + max(maxLeft, maxRight)
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSumPath = float('-inf')       
        def traversal(node):
            if not node:
                return 0
            maxLeft = max(0, traversal(node.left))
            maxRight = max(0, traversal(node.right))
            currMax = node.val + maxLeft + maxRight
            self.maxSumPath = max(self.maxSumPath, currMax)
            return node.val + max(maxLeft, maxRight)
        traversal(root)
        return self.maxSumPath