# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Date Solved: 8 June 2026, Monday
    # Not in NC250 but frequently asked
    # Refer: codestorywithMIK, Namaste DSA, NeetCode and Alvin The Programmer YouTube
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def inOrder(root, current_sum):
            if root is None:
                return False

            current_sum += root.val

            # Leaf node
            if root.left is None and root.right is None:
                if current_sum == targetSum:
                    return True
                return False

            left_side = inOrder(root.left, current_sum)
            right_side = inOrder(root.right, current_sum)

            return left_side or right_side

        return inOrder(root, 0)
