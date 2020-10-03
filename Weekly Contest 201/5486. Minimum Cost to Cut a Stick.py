import sys
from typing import List 
from functools import lru_cache

class Solution:
    # https://leetcode.com/problems/minimum-cost-to-cut-a-stick/discuss/780880/C%2B%2B-Top-Down-DP
    def minCost(self, n: int, cuts: List[int]) -> int:
        @lru_cache(None)
        def calculate_cost(n: int, start: int, end: int) -> int:
            if (end - start) <= 1:
                return 0
            ans = sys.maxsize
            for k in range(start + 1, end):
                ans1 = calculate_cost(n, start, k) 
                ans2 = calculate_cost(n, k, end)
                # print(ans, cuts[end] - cuts[start] + ans1 + ans2, "#values:", cuts[end], -cuts[start], ans1, ans2)
                               
                ans = min(ans, cuts[end] - cuts[start] + ans1 + ans2)
            return ans
        cuts = sorted(cuts +[0, n])
        return calculate_cost(n, 0, len(cuts)-1)

obj = Solution()
print( 16, obj.minCost( n = 7, cuts = [1,3,4,5] ))
print( 22, obj.minCost( n = 9, cuts = [5,6,1,4,2] ))