# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        ans = [False]  # using list to allow updates inside nested function
        def traverse(curr, currSum):
            newSum = currSum + curr.val
            if not curr.left and not curr.right:
                if newSum == targetSum:
                    ans[0] = True
            if curr.left:
                traverse(curr.left, newSum)
            if curr.right:
                traverse(curr.right, newSum)
        traverse(root, 0)
        return ans[0]