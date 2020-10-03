from typing import List
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        counter = 0
        for a in arr:
            if a%2==1:
                counter += 1
                if counter == 3:
                    return True
            else:
                counter = 0
        return False