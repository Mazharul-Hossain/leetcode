from typing import List


class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        dict = [{} for _ in range(n)]
        for i in range(len(preferences)):
            for j in range(len(preferences[i])):
                dict[i][preferences[i][j]] = j

        unhappy = 0
        for pair in pairs:
            x, y = pair
            if dict[x][y] != dict[y][x]:
                unhappy += 1
        return unhappy


obj = Solution()
print(2, obj.unhappyFriends(n=4, preferences=[[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]], pairs=[[0, 1], [2, 3]]))
print(0, obj.unhappyFriends(n=2, preferences=[[1], [0]], pairs=[[1, 0]]))
print(4, obj.unhappyFriends(n=4, preferences=[[1, 3, 2], [2, 3, 0], [1, 3, 0], [0, 2, 1]], pairs=[[1, 3], [0, 2]]))
print(0, obj.unhappyFriends(n=4, preferences=[[1, 3, 2], [2, 3, 0], [1, 0, 3], [1, 0, 2]], pairs=[[2, 1], [3, 0]]))
