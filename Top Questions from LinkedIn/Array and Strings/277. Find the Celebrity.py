# The knows API is already defined for you.
# return a bool, whether a knows b
from functools import lru_cache


def knows(a: int, b: int) -> bool:
    pass


class Solution:
    def findCelebrity(self, n: int) -> int:
        @lru_cache(maxsize=None)
        def cached_knows(a, b):
            return knows(a, b)

        def is_celebrity(a):
            for b in range(n):
                if a == b:
                    continue
                # if a knows some one or b is celebrity
                if cached_knows(a, b) or not cached_knows(b, a):
                    return False
            return True

        celebrity_candidate = 0
        for i in range(1, n):
            # if celebrity_candidate knows some one, he is not celebrity
            if cached_knows(celebrity_candidate, i):
                celebrity_candidate = i

        if is_celebrity(celebrity_candidate):
            return celebrity_candidate

        return -1
