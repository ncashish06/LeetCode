# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    def isMirror(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return (left.val == right.val and
                isMirror(left.left, right.right) and
                isMirror(left.right, right.left))
    """
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        #return self.isMirror(root.left, root.right)
        q = deque([root.left, root.right])
        while q:
            p1 = q.popleft()
            p2 = q.popleft()
            if not p1 and not p2: #if both are null then they are symmetric
                continue
            if not p1 or not p2 or p1.val != p2.val:
                return False
            q.append(p1.left)
            q.append(p2.right)
            q.append(p1.right)
            q.append(p2.left)
        return True