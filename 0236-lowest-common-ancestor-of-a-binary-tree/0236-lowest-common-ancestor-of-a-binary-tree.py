# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca = None
        # bottom-up recursion, go till null node (child of leaf node) in the tree and then traverse back up
        def traverse (curr_node):
            nonlocal lca
            count = 0
            if not curr_node:
                return 0
            is_node_on_left = traverse(curr_node.left)
            is_node_on_right = traverse(curr_node.right)
            if curr_node.val == p.val or curr_node.val == q.val:
                count+=1
            count = count + is_node_on_left + is_node_on_right
            if count == 2 and not lca: # skip updating lca as you traverse back up the tree after you have found lca
                lca = curr_node # setting lca here

            return count

        traverse(root)
        return lca


