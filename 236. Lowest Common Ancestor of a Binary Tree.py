# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == p:
            return p
        if root == q:
            return q
        left_node = None
        if root.left is not None:
            left_node = self.lowestCommonAncestor(root.left, p, q)
        
        right_node = None
        if root.right is not None:
            right_node = self.lowestCommonAncestor(root.right, p, q)

        if left_node is None:
            return right_node
        if right_node is None:
            return left_node
        return root