# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random
from collections import deque


class Solution:
    # Date Solved: 22 June 2026, Monday, Weekly Premium W4
    # Almost same solution as LC. 133 Clone Graph (Blind 75)
    # Refer: Namaste DSA (BFS)
    # Time: O(N), Space: O(N) where N = number of nodes
    def copyRandomBinaryTree(self, root: "Optional[Node]") -> "Optional[NodeCopy]":
        if not root:
            return None

        visited = {}
        q = deque([root])

        visited[root] = NodeCopy(root.val)

        while q:
            curr = q.popleft()
            cloneCurr = visited[curr]

            for neighbor in [curr.left, curr.right, curr.random]:
                if neighbor and neighbor not in visited:
                    visited[neighbor] = NodeCopy(neighbor.val)
                    q.append(neighbor)

            cloneCurr.left = visited.get(curr.left)
            cloneCurr.right = visited.get(curr.right)
            cloneCurr.random = visited.get(curr.random)

        return visited[root]
