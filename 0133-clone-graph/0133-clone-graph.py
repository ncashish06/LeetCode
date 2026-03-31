"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # This is BFS on the graph problem
        if not node:
            return None
        
        q = deque([node])
        visited = {}
        clone_root = Node(node.val)
        visited[node] = clone_root

        while len(q)>0:
            curr_node = q.popleft()
            curr_clone = visited[curr_node]
            for n in curr_node.neighbors:
                if n not in visited:
                    q.append(n)
                    visited[n] = Node(n.val)

                curr_clone.neighbors.append(visited[n])

        return clone_root
        