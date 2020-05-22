from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x=False):
        self.val = x
        self.children = []


class Solution:
    def get_root(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> TreeNode:
        node_list = [ None for _ in range(n) ]

        for edge in edges:
            from_i, to_i = edge

            if node_list[from_i] is None:
                node_list[from_i] = TreeNode( hasApple[from_i] )

            if node_list[to_i] is None:
                node_list[to_i] = TreeNode( hasApple[to_i] )

            node_list[from_i].children.append( node_list[to_i] )
        return node_list[0]

    def get_path_depth(self, root: TreeNode) -> int:
        path_depth = 0
        for node in root.children:
            path_depth += self.get_path_depth(node)
        
        if path_depth > 0 or root.val:
            path_depth += 2
        return path_depth

    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        root = self.get_root(n, edges, hasApple)

        path_depth = 0
        for node in root.children:
            path_depth += self.get_path_depth(node)

        return path_depth


obj = Solution()

print( 8, obj.minTime( n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [False,False,True,False,True,True,False] ) )
print( 6, obj.minTime( n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [False,False,True,False,False,True,False] ) )
print( 0, obj.minTime( n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [False,False,False,False,False,False,False] ) )    