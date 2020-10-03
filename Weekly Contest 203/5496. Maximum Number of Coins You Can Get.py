from typing import List


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles = sorted(piles, reverse=True)
        ans = 0
        length = len(piles) // 3
        for i in range(0, length):
            ans += piles[2 * i + 1]
        return ans


obj = Solution()
print(9, obj.maxCoins(piles=[2, 4, 1, 2, 7, 8]))
print(4, obj.maxCoins(piles=[2, 4, 5]))
print(18, obj.maxCoins(piles=[9, 8, 7, 6, 5, 1, 2, 3, 4]))
