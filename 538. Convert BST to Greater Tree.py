# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        # iterate tree and create set
        tree_list = []
        value_set = set()

        tree_list.append(root)
        while len(tree_list) > 0:
            temp_node = tree_list.pop()
            value_set.add(temp_node.val)

            if temp_node.left:
                tree_list.append(temp_node.left)
            if temp_node.right:
                tree_list.append(temp_node.right)
        value_list = list(value_set)
        value_list.sort(reverse = True)
        
        cumulative_sum = 0
        tree_hash = {}
        for i in range(len(value_list)):
            tree_hash[value_list[i]] = cumulative_sum
            cumulative_sum += value_list[i]

        tree_list = []
        tree_list.append(root)
        while len(tree_list) > 0:
            temp_node = tree_list.pop()
            temp_node.val += tree_hash[temp_node.val]
            if temp_node.left:
                tree_list.append(temp_node.left)
            if temp_node.right:
                tree_list.append(temp_node.right)
        return root

