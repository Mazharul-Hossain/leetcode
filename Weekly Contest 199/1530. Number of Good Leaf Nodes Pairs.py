# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        def inOrderTraversal(root: TreeNode):
            left_counter, right_counter, l, left_leaf, right_leaf = 0, 0, True, {}, {}
            if root.left is not None:
                l = False
                left_counter, left_leaf = inOrderTraversal(root.left)
            if root.right is not None:
                l = False
                right_counter, right_leaf = inOrderTraversal(root.right)
            
            leaf, counter = {}, left_counter + right_counter
            if l:
                leaf[str(root.val)] = 1
            else:
                left_leaf  = {k: v for k, v in sorted(left_leaf.items(),  key=lambda item: item[1])}                
                right_leaf = {k: v for k, v in sorted(right_leaf.items(), key=lambda item: item[1])}
                for k_l, v_l in left_leaf.items():
                    if v_l >= distance:
                        continue
                    for k_r, v_r in right_leaf.items():
                        if (v_l + v_r) <= distance:
                            counter += 1
                        else:
                            break
                    if v_l + 1 < distance:
                        leaf[k_l] = v_l + 1
                for k_r, v_r in right_leaf.items():
                    if v_r >= distance:
                        continue
                    while k_r in leaf:
                        k_r = str(k_r) + "_r"
                    if v_r + 1 < distance:
                        leaf[k_r] = v_r + 1                
                if counter > 0:
                    print(root.val, counter, left_leaf, right_leaf)
            return counter, leaf

        counter, _ = inOrderTraversal(root)        
        return counter