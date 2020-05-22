# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def in_order_traversal(self, root: TreeNode) -> []:
        result = []

        if root is not None:
            result.extend( self.in_order_traversal( root.left ) )
            result.append( root.val )
            result.extend( self.in_order_traversal( root.right ) )
        
        return result

    def create_balance_BST(self, sorted_list: []) -> TreeNode:
        if len(sorted_list) == 0:
            return None
        index = len(sorted_list) // 2
        print(index, sorted_list)
        root = TreeNode( sorted_list[index] )

        root.left = self.create_balance_BST( sorted_list[ : index ] )
        
        root.right = self.create_balance_BST( sorted_list[ index+1 : ] )

        return root

    def balanceBST(self, root: TreeNode) -> TreeNode:

        # in-order traversal
        sorted_list = self.in_order_traversal(root)
        print( sorted_list )

        return self.create_balance_BST(sorted_list)


root = TreeNode(1)
root.right = TreeNode(2)
root.right.right = TreeNode(3)
root.right.right.right = TreeNode(4)

obj = Solution()
root = obj.balanceBST( root )
print( root.val )