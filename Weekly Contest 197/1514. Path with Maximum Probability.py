from typing import List
from queue import PriorityQueue

class TreeNode:
    def __init__(self, x):
        self.success_prob = 0.0
        self.edge_list = {}

class Solution:
    # shortest path problem
    # https://leetcode.com/problems/path-with-maximum-probability/discuss/731767/JavaPython-3-2-codes%3A-Bellman-Ford-and-Dijkstra's-algorithm-w-brief-explanation-and-analysis.
    
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        node_list = [TreeNode(i) for i in range(n)]

        for i in range( len(edges ) ):
            a, b = edges[i]
            if node_list[a] is None:
                node_list[a] = TreeNode(a)
            if node_list[b] is None:
                node_list[b] = TreeNode(b)
            node_list[a].edge_list[b] = succProb[i]            
            node_list[b].edge_list[a] = succProb[i]

        bfs_list, node_list[start].success_prob = PriorityQueue(), 1.0
        bfs_list.put( ( -1.0, start ) )
        while bfs_list.qsize() > 0 :
            _, head = bfs_list.get()            
            if head == end:
                break
            for node, weight in node_list[head].edge_list.items():
                temp_prob = node_list[head].success_prob * weight
                if temp_prob > node_list[node].success_prob:
                    node_list[node].success_prob = temp_prob
                    bfs_list.put( (-temp_prob, node) )

        return node_list[end].success_prob


obj = Solution()
print( obj.maxProbability( n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2))
print( obj.maxProbability( n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2))
print( obj.maxProbability( n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2))
print( obj.maxProbability( 500, [[193,229],[133,212],[224,465]], [0.91,0.78,0.64], 4, 364) )