# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Date Solved: 11 June 2026, Thursday
    # Refer: codestorywithMIK
    # Blind 75
    # This code used in 11 June 2026 POTD, LC. 3558 Number of Ways to Assign Edge Weights I
    # Time: O(N), Space: O(N) when tree is unbalanced
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Bottom up recursion approach
        if not root:
            return 0
        left_max_depth = self.maxDepth(root.left)
        right_max_depth = self.maxDepth(root.right)
        return 1 + max(left_max_depth, right_max_depth)
        """
        # Top down recursion approach
        if not root:
            return 0
        self.max_depth = 0
        def traversal(curr_node, depth):
            self.max_depth = max(self.max_depth, depth)
            if curr_node.left:
                traversal(curr_node.left, depth + 1)
        
            if curr_node.right:
                traversal(curr_node.right, depth + 1)
        
        traversal(root, 1)
        return self.max_depth
        """
