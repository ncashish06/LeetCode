# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # Date Solved: 30 June 2026, Tuesday
    # Refer: codestorywithMIK, NeetCode (no video, only solution) and Namaste DSA
    # Not in NC250 but LC. 235 LCA of BST is Blind 75
    # This problem can also be solved using Binary Lifting Technique (Jumping up in the powers of 2 instead of one jump at a time) but is overkill.
    # Refer: codestorywithMIK Binary Lifting (DP) playlist, 3rd of 4 videos
    def lowestCommonAncestor(self, root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
        # Base Case: If we hit a null node or find p or q, return it up
        if root is None or root is p or root is q:
            return root

        # Search left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # 1. If both left and right are non-null, this root IS the LCA
        if left and right:
            return root

        # 2. If only one is non-null, pass that result up (it's either a target or the LCA)
        return left if left else right
