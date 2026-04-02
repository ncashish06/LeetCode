"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        def traversal(curr):
            if curr.left:
                curr.left.next = curr.right
            if curr.right and curr.next:
                curr.right.next = curr.next.left
            if curr.left:
                traversal(curr.left)
            if curr.right:
                traversal(curr.right)
        traversal(root)
        return root