from typing import List


def zeros_at_end(grid: List[List[int]]):
    zeros_dict = {}
    for r in range(len(grid)):
        counter, row = 0, grid[r]
        for i in range(len(row) - 1, 0, -1):
            if row[i] == 0:
                counter += 1
            else:
                break
        zeros_dict[r] = counter
    return zeros_dict


class Solution:

    def minSwaps(self, grid: List[List[int]]) -> int:
        zeros_dict = zeros_at_end(grid)
        # print(zeros_dict)

        n, ans = len(zeros_dict), 0

        for i in range(n):
            if zeros_dict[i] < (n - i - 1):
                j = i
                while j < n and zeros_dict[j] < (n - i - 1):
                    j += 1

                if j == n:
                    # Did not find any number greater than or equal to n-i-1.
                    return -1  # so its impossible to get the answer

                while j > i:
                    # swap(a[j], a[j-1]);
                    temp = zeros_dict[j]
                    zeros_dict[j] = zeros_dict[j - 1]
                    zeros_dict[j - 1] = temp
                    ans += 1
                    j -= 1
        return ans


obj = Solution()
print(3, obj.minSwaps(grid=[[0, 0, 1], [1, 1, 0], [1, 0, 0]]))
print(-1, obj.minSwaps(grid=[[0, 1, 1, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 1, 1, 0]]))
print(0, obj.minSwaps(grid=[[1, 0, 0], [1, 1, 0], [1, 1, 1]]))
