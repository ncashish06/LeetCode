# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Date Solved: 11 June 2026, Thursday
    # Refer: Alvin The Programmer YouTube
    # Time: O(N), Space: O(N) when tree is unbalanced
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return self._minDepth(root)

    def _minDepth(self, root: Optional[TreeNode]) -> int:
        # Bottom up recursion approach
        if not root:
            return float("inf")
        if not root.left and not root.right:
            return 1
        left_min_depth = self._minDepth(root.left)
        right_min_depth = self._minDepth(root.right)
        return 1 + min(left_min_depth, right_min_depth)
