from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/discuss/34538/My-Accepted-Java-Solution
    def find_key_by_value(self, list: List[int], value: int):
        for key in range(len(list)):
            if list[key] == value:
                return key

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # preorder: ROOT L   R
        # inorder : L    ROOT R
        if preorder is None and inorder is None:
            return None
        if len(preorder) == 0 and len(inorder) == 0:
            return None

        head = TreeNode(preorder[0])
        head_in_order = self.find_key_by_value(inorder, preorder[0])
        if head_in_order == 0:
            head.left = None
        else:            
            head.left = self.buildTree(preorder[1:head_in_order+1], inorder[:head_in_order] )
        
        if (head_in_order+1) >= len(preorder):
            head.right = None
        else:
            head.right = self.buildTree(preorder[head_in_order+1:], inorder[head_in_order+1:] )
        
        return head

obj = Solution()
# head = obj.buildTree( preorder = [3,9,2], inorder = [9,2,3])
head = obj.buildTree( preorder = [3,9,1], inorder = [1,9,3])
print( head.val )