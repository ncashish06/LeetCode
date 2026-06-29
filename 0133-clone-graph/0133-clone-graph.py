"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import deque


class Solution:
    # Date Solved: 22 June 2026, Monday
    # Blind 75
    # Refer: Namaste DSA (BFS)
    # Time: O(V+E), Space: O(V)
    # Similar solution for LC. 1485 Clone Binary Tree with Random Pointer and LC. 1490 Clone N-ary Tree
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return None

        visited = {}
        q = deque([node])

        visited[node] = Node(node.val)

        while q:
            curr = q.popleft()
            cloneCurr = visited[curr]

            for neighbor in curr.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                cloneCurr.neighbors.append(visited[neighbor])

        return visited[node]
