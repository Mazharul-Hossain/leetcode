from typing import List
MODULO_VALUE=1000000007
class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort(), verticalCuts.sort()

        max_h, pointer = 0, 0
        for i in horizontalCuts:            
            temp_h = i - pointer
            # print(temp_h, i, pointer)

            max_h = max(max_h, temp_h)
            pointer = i
        temp_h = h - pointer
        # print(temp_h, h, pointer)
        max_h = max(max_h, temp_h)

        max_w, pointer = 0, 0
        for i in verticalCuts:
            temp_w = i - pointer
            # print(temp_w, i, pointer)

            max_w = max(max_w, temp_w)
            pointer = i
        temp_w = w - pointer
        # print(temp_w, w, pointer)
        max_w = max(max_w, temp_w)

        return ( (max_h % MODULO_VALUE) * (max_w % MODULO_VALUE) ) % MODULO_VALUE


obj = Solution()
# print( 4, obj.maxArea( h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3] ) )
print( 6, obj.maxArea( h = 5, w = 4, horizontalCuts = [3,1], verticalCuts = [1] ) )
# print( 9, obj.maxArea( h = 5, w = 4, horizontalCuts = [3], verticalCuts = [3] ) )