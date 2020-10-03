from typing import List
class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        dict = {}
        for r in range(len(grid)):            
            counter, row = 0, grid[r]
            for i in range(len(row)-1, 0, -1):
                if row[i] == 0:
                    counter += 1
                else:
                    break
            dict[r] = counter
