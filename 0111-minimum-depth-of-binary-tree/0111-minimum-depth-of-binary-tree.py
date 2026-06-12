# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    # Date Solved: 11 June 2026, Thursday
    # Refer: codestorywithMIK
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # Approach 1: DFS
        # Time: O(N), Space: O(N) when tree is unbalanced
        if not root:
            return 0

        if root.left is None and root.right is None:
            return 1

        left = self.minDepth(root.left) if root.left else float("inf")
        right = self.minDepth(root.right) if root.right else float("inf")

        return 1 + min(left, right)
        """
        # Approach 2: BFS
        # Time: O(N), Space: O(N)
        if not root:
            return 0

        if not root.left and not root.right:
            return 1

        queue = deque([root])
        depth = 1

        while queue:
            n = len(queue)

            for _ in range(n):
                temp = queue.popleft()

                if not temp.left and not temp.right:
                    return depth

                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)

            depth += 1

        return -1
        """
