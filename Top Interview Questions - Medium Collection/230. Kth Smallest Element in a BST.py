# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inOrderTraversal(self, root: TreeNode, k: int):
        # in-order traversal 
        temp_k, temp_val = 0, 0
        
        # going to left
        if root.left is not None:
            temp_k, temp_val = self.inOrderTraversal(root.left, k)
        if temp_k == k:
            return temp_k, temp_val
        
        # counting self
        temp_k += 1
        temp_val = root.val
        if temp_k == k:
            return temp_k, temp_val
        
        # going to right
        if root.right is not None:
            temp_k_r, temp_val_r = self.inOrderTraversal(root.right, k-temp_k)
            temp_k += temp_k_r
            temp_val = temp_val_r
        
        return temp_k, temp_val
        

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        _, temp_val = self.inOrderTraversal(root, k)
        return temp_val