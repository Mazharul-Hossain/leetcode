from queue import PriorityQueue
from typing import List

from libDisjointSets import DisjointSets


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        ds = DisjointSets()
        cost_priority_queue = PriorityQueue()
        cost = 0
        if len(points) > 1:
            for i in range(len(points)):
                for j in range(i + 1, len(points)):
                    dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                    # print(points[i], points[j], dist)
                    cost_priority_queue.put((dist, (i, j)))
            counter, points_set = len(points) - 1, set()

            # print("\nNow solving: ")
            while counter > 0 and cost_priority_queue.qsize() > 0:
                dist, point = cost_priority_queue.get()
                point_i, point_j = point
                # print(points[point_i], points[point_j], dist)

                ds.make_set(point_i)
                ds.make_set(point_j)
                if ds.find_set_int(point_i) != ds.find_set_int(point_j):
                    cost += dist
                    ds.union_int(point_i, point_j)
                    counter -= 1
        return cost


obj = Solution()
print(20, obj.minCostConnectPoints(points=[[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]))
print(18, obj.minCostConnectPoints(points=[[3, 12], [-2, 5], [-4, 1]]))
print(4, obj.minCostConnectPoints(points=[[0, 0], [1, 1], [1, 0], [-1, 1]]))
print(4000000, obj.minCostConnectPoints(points=[[-1000000, -1000000], [1000000, 1000000]]))
print(0, obj.minCostConnectPoints(points=[[0, 0]]))
print(53, obj.minCostConnectPoints([[2, -3], [-17, -8], [13, 8], [-17, -15]]))
