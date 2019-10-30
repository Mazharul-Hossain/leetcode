# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    ################
    # does not work
    ################
    # def inorder_traversal(self, root):
    #     result_list = []        
    #     if root.left is not None:
    #         result_list = self.inorder_traversal(root.left)
        
    #     result_list.append(root.val)
        
    #     if root.right is not None:
    #         result_list.extend(self.inorder_traversal(root.right) )
        
    #     return result_list

    # def isSymmetric(self, root: TreeNode) -> bool:
    #     if root is not None:
    #         result_list = self.inorder_traversal(root)

    #         right_position = len(result_list) - 1
    #         left_position = 0
    #         while(right_position > left_position):
    #             if result_list[left_position] == result_list[right_position]:
    #                 left_position, right_position = left_position + 1, right_position - 1
    #             else:
    #                 return False
    #         return True
    #     return False

    ####################
    # recursive solution
    ####################
    # def null_check(self, left, right):
    #     if left is None and right is None:
    #         return True
    #     if left is None:
    #         return False
    #     if right is None:
    #         return False
    #     if left.val == right.val:
    #         return True
    #     return False
    
    # def compare_symmetric(self, left, right):
    #     if self.null_check(left.left, right.right):
    #         if left.left is not None and right.right is not None:
    #             if not self.compare_symmetric(left.left, right.right):
    #                 return False
    #     else:
    #         return False

    #     if self.null_check(left.right, right.left):
    #         if left.right is not None and right.left is not None:
    #             if not self.compare_symmetric(left.right, right.left):
    #                 return False
    #     else:
    #         return False
    #     return True        

    # def isSymmetric(self, root: TreeNode) -> bool:
    #     if root is not None:
    #         if self.null_check(root.left, root.right):
    #             if root.left is None and root.right is None:
    #                 return True
    #             else:
    #                 return self.compare_symmetric(root.left, root.right)   
    #         else:
    #             return False 
    #     return True    

    ################
    # iterative solution
    ################
    def isSymmetric(self, root: TreeNode) -> bool:
        import queue
        left_list, right_list = queue.Queue(), queue.Queue()
        if root is not None:
            left_list.put(root.left)
            right_list.put(root.right)

            while(not left_list.empty() and not right_list.empty()):
                left, right = left_list.get(), right_list.get()
                if left is None and right is None:
                    continue
                if left is None:
                    return False
                if right is None:
                    return False
                if left.val == right.val:
                    left_list.put(left.left)
                    right_list.put(right.right)

                    left_list.put(left.right)
                    right_list.put(right.left)
                else:
                    return False
        return True    