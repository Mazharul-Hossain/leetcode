import copy
from typing import List

class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        self.island_disconnection_point  = []
        def countNumberOfIslands(x: int, y: int, m: int, n: int):
            grid[x][y] = 2
            count_x, count_y = 0, 0
            if x > 0 and (grid[x-1][y] == 1 or grid[x-1][y] == 2):
                count_x += 1
            if x < (m - 1) and (grid[x+1][y] == 1 or grid[x+1][y] == 2):
                count_x += 1

            if y > 0 and (grid[x][y-1] == 1 or grid[x][y-1] == 2):
                count_y += 1
            if y < (n - 1) and (grid[x][y+1] == 1 or grid[x][y+1] == 2):
                count_y += 1
            
            if count_x == 0 or count_y == 0:
                self.island_flag = True
            elif (count_x + count_y) <= 1:
                self.island_flag = True

            if x > 0 and grid[x-1][y] == 1:
                countNumberOfIslands(x-1, y, m, n)
            if x < (m - 1) and grid[x+1][y] == 1:
                countNumberOfIslands(x+1, y, m, n)

            if y > 0 and grid[x][y-1] == 1:
                countNumberOfIslands(x, y-1, m, n)
            if y < (n - 1) and grid[x][y+1] == 1:
                countNumberOfIslands(x, y+1, m, n)
        
        island_count, m, n = 0, len(grid), len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    island_count += 1
                    countNumberOfIslands(i, j, m, n)
        # print(island_count, self.island_flag)
        if island_count != 1:
            return 0        
        if self.island_flag:
            return 1
        else:
            return 2

obj = Solution()
print(2, obj.minDays(grid = [
    [0,1,1,0],
    [0,1,1,0],
    [0,0,0,0]]))
print(2, obj.minDays(grid = [[1,1]]))
print(0, obj.minDays(grid = [[1,0,1,0]]))
print(1, obj.minDays(grid = [
               [1,1,0,1,1],
               [1,1,1,1,1],
               [1,1,0,1,1],
               [1,1,0,1,1]]))
print(2, obj.minDays(grid = [
               [1,1,0,1,1],
               [1,1,1,1,1],
               [1,1,0,1,1],
               [1,1,1,1,1]]))