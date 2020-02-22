class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0

        for row in grid:
            for i in range(len(row) - 1, -1, -1 ):
                if row[i] < 0:
                    count += 1
                else:
                    break

        return count