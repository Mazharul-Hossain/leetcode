# TLE
# class Solution:
#     def __init__(self):
#         self.path = 0
#
#     def uniquePaths(self, m: int, n: int) -> int:
#         self.path = 0
#
#         def path_computation(a: int, b: int):
#             if a == m and b == n:
#                 self.path += 1
#                 return
#             if a < m:
#                 path_computation(a + 1, b)
#
#             if b < n:
#                 path_computation(a, b + 1)
#
#         path_computation(1, 1)
#         return self.path
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        answer = [1 for _ in range(n)]
        for _ in range(1, m):
            for i in range(1, n):
                answer[i] += answer[i - 1]
        return answer[n - 1]


obj = Solution()
print(28, obj.uniquePaths(m=3, n=7))
print(3, obj.uniquePaths(m=3, n=2))
print(28, obj.uniquePaths(m=7, n=3))
print(6, obj.uniquePaths(m=3, n=3))
