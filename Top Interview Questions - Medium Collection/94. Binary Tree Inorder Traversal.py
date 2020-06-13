from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        list = []
        if root is not None:
            if root.left is not None:
                list += self.inorderTraversal(root.left)
            list.append(root.val)
            if root.right is not None:
                list += self.inorderTraversal(root.right)
        return list

