import heapq
import sys
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        dist = [[sys.maxsize] * n for _ in range(m)]
        minHeap = [(0, 0, 0)]
        DIR = [0, 1, 0, -1, 0]
        while minHeap:
            d, r, c = heapq.heappop(minHeap)
            if r == m - 1 and c == n - 1:
                return d  # Reach to bottom right
            for i in range(4):
                nr, nc = r + DIR[i], c + DIR[i + 1]
                if 0 <= nr < m and 0 <= nc < n:
                    newDist = max(d, abs(heights[nr][nc] - heights[r][c]))
                    if dist[nr][nc] > newDist:
                        dist[nr][nc] = newDist
                        heapq.heappush(minHeap, (dist[nr][nc], nr, nc))
