from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # https://leetcode.com/problems/number-of-islands/discuss/56359/Very-concise-Java-AC-solution
        def getAllPartOfIsland(i, j):
            grid[i][j] = 0
            if j+1 < len(grid[i]) and grid[i][j+1] == '1':
                getAllPartOfIsland(i, j+1)
            if i+1 < len(grid) and grid[i+1][j] == '1':
                getAllPartOfIsland(i+1, j)

            if j>0 and grid[i][j-1] == '1':
                getAllPartOfIsland(i, j-1)
            if i>0 and grid[i-1][j] == '1':
                getAllPartOfIsland(i-1, j)

        numOfIslands = 0
        if grid is not None:
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    if grid[i][j] == '1':
                        numOfIslands += 1
                        getAllPartOfIsland(i, j)          
        return numOfIslands

obj = Solution()
print(1, obj.numIslands( grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))
print(3, obj.numIslands( grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))