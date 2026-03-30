# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # BFS level order traversal
        if not root:
            return []
        
        ans = []
        q = deque([root]) # O(1) lefft pop with deque compared to O(n) with list (q_list.pop(0) is O(n), shifts rest of elements)
        
        while q:
            level_size = len(q)
            for i in range(level_size):
                curr = q.popleft()
                
                # Since we append right child first, i == 0 is the rightmost node
                if i == 0:
                    ans.append(curr.val)
                
                # Standard BFS level order traversal but prioritizing the right side
                if curr.right:
                    q.append(curr.right)
                if curr.left:
                    q.append(curr.left)
                    
        return ans