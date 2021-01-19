import sys
from functools import lru_cache


class Solution:
    @lru_cache(None)
    def minDays(self, n: int, counter: int = 0) -> int:
        if n == 1:
            return 1
        days = sys.maxsize
        if n % 3 == 0:
            temp_days = self.minDays(n // 3, counter=0)
            days = min(days, temp_days)

        if n % 2 == 0:
            temp_days = self.minDays(n // 2, counter=0)
            days = min(days, temp_days)

        if counter < 2:
            temp_days = self.minDays(n - 1, counter=counter + 1)
            days = min(days, temp_days)

        return days + 1


obj = Solution()
print(4, obj.minDays(n=10))
print(3, obj.minDays(n=6))
print(1, obj.minDays(n=1))
print(6, obj.minDays(n=56))
