from typing import List

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()

        distance = arr[1] - arr[0]
        for i in range(2, len(arr)):
            if arr[i] != arr[i-1] + distance:
                return False
        return True