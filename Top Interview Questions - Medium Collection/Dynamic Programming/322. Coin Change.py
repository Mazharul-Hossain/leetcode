import sys
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [sys.maxsize] * amount
        coins.sort(reverse=True)

        for i in range(1, amount + 1):
            for c in coins:
                if i >= c:
                    dp[i] = min(dp[i - c] + 1, dp[i])
        return [dp[amount], -1][dp[amount] == sys.maxsize]


obj = Solution()
print(3, obj.coinChange(coins=[1, 2, 5], amount=11))
print(-1, obj.coinChange(coins=[2], amount=3))
print(0, obj.coinChange(coins=[1], amount=0))
print(1, obj.coinChange(coins=[1], amount=1))
print(2, obj.coinChange(coins=[1], amount=2))
