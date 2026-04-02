# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = deque([root])
        level = 0
        while q:
            size = len(q)
            level_nodes = deque()
            for _ in range(size):
                node = q.popleft()
                if level % 2 == 0:
                    level_nodes.append(node.val)
                else:
                    level_nodes.appendleft(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(list(level_nodes))
            level += 1
        return res