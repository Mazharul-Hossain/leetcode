# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # if root is a list
        # multiplier, move = 1, 0
        # while (move+multiplier) < len(root):
        #     root = root[:move+multiplier] + ['#'] + root[move+multiplier:]
        #     multiplier *= 2
        #     move += multiplier
        # return root + ['#']        
        
        node_list, temp_list = [], [root]
        while len(temp_list) > 0:
            node_list, temp_node = temp_list, None
            temp_list = []
            while len(node_list) > 0:
                node = node_list.pop(0)
                
                if node is None or node.left is None:
                    continue
                if temp_node is not None:
                    temp_node.next = node.left
                node.left.next = node.right
                temp_list.append(node.left)

                node.right.next = None
                temp_node = node.right
                temp_list.append(node.right)
        return root



obj = Solution()
# print( obj.connect( root = [1,2,3,4,5,6,7] ) )