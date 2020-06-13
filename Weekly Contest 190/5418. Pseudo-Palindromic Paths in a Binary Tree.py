# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode, number_dictionary=None) -> int:
        if number_dictionary is None:
            number_dictionary = {}

        path = 0
        if root.val in number_dictionary:
            del number_dictionary[root.val]
        else:
            number_dictionary[root.val] = 1
        
        if root.left is None and root.right is None:
            if len(number_dictionary) <= 1:
                path = 1
        else:
            if root.left is not None:
                path += self.pseudoPalindromicPaths(root.left, number_dictionary.copy())
            if root.right is not None:
                path += self.pseudoPalindromicPaths(root.right, number_dictionary.copy())
        
        return path 