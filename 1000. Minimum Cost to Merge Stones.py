import sys
from typing import List
from functools import lru_cache

class Solution:
    def mergeStones(self, stones: List[int], K: int) -> int:
        @lru_cache(None)
        def mergeKStones(temp_stones: List[int]):
            if len(temp_stones) < K:
                return 0, temp_stones
            keep_me_out = temp_stones.pop(0)
            cost_1, temp_stones_1 = mergeKStones(temp_stones)
            temp_stones_1 = [keep_me_out] + temp_stones_1
            if len(temp_stones_1) >= K:
                sum, counter = 0, K
                while counter > 0:
                    sum += temp_stones_1.pop(0)
                    counter -= 1
                temp_stones_1 = [sum] + temp_stones_1
                cost_1 += sum

            temp_stones = [keep_me_out] + temp_stones
            sum, counter = 0, K
            while counter > 0:
                sum += temp_stones.pop(0)
                counter -= 1
            temp_stones = [sum] + temp_stones
            cost = sum
            cost_2, temp_stones_2 = mergeKStones(temp_stones)
            cost_2 += cost

            if cost_1 > cost_2:
                return cost_2, temp_stones_2
            else:
                cost_1, temp_stones_1

        cost, temp_stones = mergeKStones(stones)
        if len(temp_stones) <= 1:
            return cost
        else:
            return -1

obj = Solution()
print( 20, obj.mergeStones( stones = [3,2,4,1], K = 2 ))
print( -1, obj.mergeStones( stones = [3,2,4,1], K = 3 ))
print( 25, obj.mergeStones( stones = [3,5,1,2,6], K = 3 ))