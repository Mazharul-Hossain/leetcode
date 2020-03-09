class TreeNode:
    def __init__(self):
        self.visited   = False
        self.left  = None
        self.right = None

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: [int], rightChild: [int]) -> bool:
        node_list = [ None for _ in range(n) ]

        for i in range(n):
            if node_list[i] is None:
                node_list[i] = TreeNode()
            
            left = leftChild[i]
            if left == 0:
                return False
            if left > 0:
                if node_list[left] is None:
                    node_list[left] = TreeNode()
                node_list[i].left = left

            right = rightChild[i]
            if right == 0:
                return False
            if right > 0:
                if node_list[right] is None:
                    node_list[right] = TreeNode()
                node_list[i].right = right

        visited_list = []
        visited_list.append(0)

        while(len(visited_list) > 0):
            visited = visited_list.pop(0)

            if node_list[visited].visited is True:
                return False
            node_list[visited].visited = True

            if node_list[visited].left is not None:
                visited_list.append(node_list[visited].left)
            if node_list[visited].right is not None:
                visited_list.append(node_list[visited].right)
        
        for node in node_list:
            if node.visited is False:
                return False
        
        return True

obj = Solution()
print(obj.validateBinaryTreeNodes(4, [1,-1,3,-1],       [2,-1,-1,-1] ) )
print(obj.validateBinaryTreeNodes(4, [1,-1,3,-1],       [2,3,-1,-1] ) )
print(obj.validateBinaryTreeNodes(2, [1,0],             [-1,-1] ) )
print(obj.validateBinaryTreeNodes(6, [1,-1,-1,4,-1,-1], [2,-1,-1,5,-1,-1] ) )