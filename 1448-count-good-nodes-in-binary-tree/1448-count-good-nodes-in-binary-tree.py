# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #DFS traversal from root
        self.ans = 0
        
        def traversal(curr, max_seen_so_far):
            if not curr:
                return
            if curr.val >= max_seen_so_far:
                self.ans += 1
            curr_max = max(max_seen_so_far, curr.val)
            traversal(curr.left, curr_max)
            traversal(curr.right, curr_max)
        
        traversal(root, float('-inf'))
        return self.ans