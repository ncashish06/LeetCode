# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # Date Solved: 30 June 2026, Tuesday
    # Refer: Namaste DSA, NeetCode and codestorywithMIK
    # Blind 75.
    # LC. 235 LCA of Binary Tree (not in NC250) solution will work for this BST problem as well.
    # This problem can also be solved using Binary Lifting Technique (Jumping up in the powers of 2 instead of one jump at a time) but is overkill.
    # Refer: codestorywithMIK Binary Lifting (DP) playlist, 3rd of 4 videos
    def lowestCommonAncestor(self, root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
        # Approach 1: Recursion
        # Time: O(h) or O(logn) for average case where h = height of the tree.  O(n) worst case : skewed BST.
        # Space: O(h) or O(logn) for average case where h = height of the tree.  O(n) worst case : skewed BST.
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
        """
        # Approach 2: Iteration
        # Time: O(h) or O(logn) for average case where h = height of the tree.  O(n) worst case : skewed BST.
        # Space: O(1)
        cur = root

        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur
        """