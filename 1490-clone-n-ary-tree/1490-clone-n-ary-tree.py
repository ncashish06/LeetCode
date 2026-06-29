"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

from collections import deque


class Solution:
    # Date Solved: 29 June 2026, Monday, Weekly Premium W5
    # Almost same solution as LC. 133 Clone Graph (Blind 75) and LC. 1485 Clone Binary Tree with Random Pointer (previous week's Weekly Premium)
    # Refer: Namaste DSA (BFS)
    # Time: O(N) Each node is visited exactly once in the BFS. For each node, we iterate over its children once. Total work across all nodes = total number of edges = N-1
    # Space: O(N)
    def cloneTree(self, root: "Node") -> "Node":
        if not root:
            return None

        visited = {}
        q = deque([root])
        visited[root] = Node(root.val)

        while q:
            curr = q.popleft()
            cloneCurr = visited[curr]

            for child in curr.children:  # N-ary: iterate children list
                if child not in visited:
                    visited[child] = Node(child.val)
                    q.append(child)
                cloneCurr.children.append(visited[child])

        return visited[root]
