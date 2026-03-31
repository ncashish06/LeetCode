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
        # This is BFS and DFS on the graph problem. 99% same code for code. See comments
        if not node:
            return None
        
        # q = deque([node]) # BFS
        stack = deque([node]) #DFS
        visited = {}
        clone_root = Node(node.val)
        visited[node] = clone_root

        while stack: # while q: #for BFS
            curr_node = stack.pop() #curr_node = q.popleft() #for BFS
            curr_clone = visited[curr_node]
            for n in curr_node.neighbors:
                if n not in visited:
                    stack.append(n) #q.append(n) #for BFS
                    visited[n] = Node(n.val)

                curr_clone.neighbors.append(visited[n])

        return clone_root
        