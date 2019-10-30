# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def depthOfBinaryTree(self, root: TreeNode):
        depth, diameter = 0, 0
        if root.left is not None or root.right is not None:        
            depth_l, diameter_l = 0, 0
            if root.left is not None:
                depth_l, diameter_l = self.depthOfBinaryTree(root.left)
            
            depth_r, diameter_r = 0, 0
            if root.right is not None:
                depth_r, diameter_r = self.depthOfBinaryTree(root.right)

            if depth_l > depth_r:
                depth = depth_l
            else:
                depth = depth_r
            
            if diameter_l > diameter_r:
                diameter = diameter_l
            else:
                diameter = diameter_r
            
            if depth_l + depth_r > diameter:
                diameter = depth_l + depth_r
        return depth + 1, diameter

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        diameter = 0
        if root is not None:
            _, diameter = self.depthOfBinaryTree(root)
        return diameter