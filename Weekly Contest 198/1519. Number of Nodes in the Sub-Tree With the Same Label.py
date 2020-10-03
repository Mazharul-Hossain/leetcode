import collections
from typing import List 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, label=""):
        self.val = val
        self.label = label
        self.is_visited = False
        self.children = []

class Solution:
    def InOrderTreeTraversal(self, root: int, node_list: List[TreeNode], result_labels):
        node_list[root].is_visited = True
        root = node_list[root]
        
        # Counter class to count in every label
        label_list = collections.Counter()
        for node in root.children:
            if node_list[node].is_visited:
                continue
            temp_label_list, result_labels = self.InOrderTreeTraversal(node, node_list, result_labels)
            label_list += temp_label_list
        label_list[root.label] += 1
        result_labels[root.val] = label_list[root.label]
        
        # print(root.val, label_list, result_labels)
        return label_list, result_labels

    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        node_list = [ TreeNode(i, labels[i]) for i in range(n)]
        # initialize the return information
        result_labels = [0 for _ in range(n)]
        for edge in edges:
            a, b = edge
            node_list[a].children.append(b)
            node_list[b].children.append(a)
        
        for i in range(n):
            if node_list[i].is_visited:
                continue
            _, result_labels = self.InOrderTreeTraversal(i, node_list, result_labels)
        return result_labels

obj = Solution()
print( [2,1,1,1,1,1,1], obj.countSubTrees( n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], labels = "abaedcd") )
print( [4,2,1,1], obj.countSubTrees( n = 4, edges = [[0,1],[1,2],[0,3]], labels = "bbbb") )
print( [3,2,1,1,1],  obj.countSubTrees(n = 5, edges = [[0,1],[0,2],[1,3],[0,4]], labels = "aabab") )
print( [1,2,1,1,2,1], obj.countSubTrees(  n = 6, edges = [[0,1],[0,2],[1,3],[3,4],[4,5]], labels = "cbabaa" ) )
print( [6,5,4,1,3,2,1], obj.countSubTrees( n = 7, edges = [[0,1],[1,2],[2,3],[3,4],[4,5],[5,6]], labels = "aaabaaa" ) )
print( [1,1,2,1], obj.countSubTrees( n = 4, edges= [[0,2],[0,3],[1,2]], labels= "aeed") )