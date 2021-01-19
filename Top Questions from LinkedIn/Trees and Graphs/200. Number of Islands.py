from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0

        def dfs(a: int, b: int):
            if a > 0 and grid[a - 1][b] == '1':
                grid[a - 1][b] = '0'
                dfs(a - 1, b)
            if a < len(grid) - 1 and grid[a + 1][b] == '1':
                grid[a + 1][b] = '0'
                dfs(a + 1, b)

            if b > 0 and grid[a][b - 1] == '1':
                grid[a][b - 1] = '0'
                dfs(a, b - 1)
            if b < len(grid[a]) - 1 and grid[a][b + 1] == '1':
                grid[a][b + 1] = '0'
                dfs(a, b + 1)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    islands += 1
                    grid[i][j] = '0'
                    dfs(i, j)
        return islands
