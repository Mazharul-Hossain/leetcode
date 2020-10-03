from typing import List
from functools import lru_cache

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        # https://leetcode.com/problems/stone-game-v/discuss/806723/C%2B%2B-Prefix-Sum-%2B-DP-(Memoization)
        # https://leetcode.com/problems/stone-game-v/discuss/806717/Java-Detailed-Explanation-Easy-Understand-DFS-%2B-Memo-Top-Down-DP
        prefixSum = [0]

        @lru_cache(None)
        def dp(left: int,right: int):
            if left == right:
                return 0
            ans = 0
            for p in range(left+1, right+1):
                left_sum, right_sum = prefixSum[p] - prefixSum[left], prefixSum[right+1] - prefixSum[p]
                # print("dp left={} p={} right={} left_sum={} right_sum= {}".format(left,p,right,left_sum,right_sum))
                if left_sum < right_sum:
                    ans = max( ans, left_sum + dp(left, p-1) )
                elif left_sum > right_sum:
                    ans = max( ans , right_sum + dp(p, right) )
                else:
                    ans = max( ans, left_sum + max( dp(left, p-1), dp(p, right) ) )
            # print(left, right, ans)
            return ans

        for i in range( len(stoneValue)):
            prefixSum.append(prefixSum[i]+stoneValue[i])
        return dp(0, len(stoneValue)-1)

obj = Solution()
print(18, obj.stoneGameV( stoneValue = [6,2,3,4,5,5]))
print(28, obj.stoneGameV( stoneValue = [7,7,7,7,7,7,7]))
print(0,  obj.stoneGameV( stoneValue = [4]))