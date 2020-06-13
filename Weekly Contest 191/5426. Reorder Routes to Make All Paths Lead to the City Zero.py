from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.child = []

        self.reverse = []
        self.visited = "RED"

class Solution:

    def build_tree(self, connections: List[List[int]]):
        node_dict = {}
        for edge in connections:
            a, b = edge
            if a not in node_dict:
                node_dict[a] = TreeNode(a)
            if b not in node_dict:
                node_dict[b] = TreeNode(b)
            node_dict[b].child.append(node_dict[a])
            node_dict[a].reverse.append(node_dict[b])
        return node_dict

    def dfs(self, root: TreeNode) -> int:
        reorder_count = 0
        for node in root.child:
            if node.visited == "RED":
                node.visited = "GREEN"
                reorder_count += self.dfs(node)
        
        for node in root.reverse:
            if node.visited == "RED":
                node.visited = "YELLOW"
                reorder_count += 1
                reorder_count += self.dfs(node)
        return reorder_count

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        node_dict = self.build_tree(connections)

        reorder_count = 0
        node_dict[0].visited = "GREEN"
        for node in node_dict[0].child:
            if node.visited == "RED":
                node.visited = "GREEN"
                reorder_count += self.dfs(node)
        
        for node in node_dict[0].reverse:
            if node.visited == "RED":
                node.visited = "YELLOW"
                reorder_count += 1
                reorder_count += self.dfs(node)
        return reorder_count

            


obj = Solution()
print( 3, obj.minReorder( n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]] ) )
print( 2, obj.minReorder( n = 5, connections = [[1,0],[1,2],[3,2],[3,4]] ) )
print( 0, obj.minReorder( n = 3, connections = [[1,0],[2,0]] ) )