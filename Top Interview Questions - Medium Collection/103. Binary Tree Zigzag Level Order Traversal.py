from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        result, flag = [], False
        if root is not None:
            temp_queue = [root]
            while len(temp_queue) > 0:
                queue = temp_queue
                temp_queue, temp_result = [], []

                for head in queue:
                    if head.left is not None:
                        temp_queue.append(head.left)
                    if head.right is not None:
                        temp_queue.append(head.right)
                    temp_result.append(head.val)  
                if flag:
                    temp_result.reverse()
                result.append(temp_result)
                flag = not flag
        return result