from typing import List

class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        # https://leetcode.com/problems/the-k-strongest-values-in-an-array/discuss/674384/C%2B%2BJavaPython-Two-Pointers-%2B-3-Bonuses
        arr.sort()
        length, median = len(arr), arr[ ( len(arr)-1 ) // 2 ]

        start, end = 0, length-1
        while start + (length-end) <= k:
            if abs( arr[start] - median ) > abs( arr[end] - median ) :
                start += 1
            else:
                end -= 1
        return arr[end+1:] + arr[:start]

obj = Solution()
print( [5,1], obj.getStrongest( arr = [1,2,3,4,5], k = 2 ) )
print( [5,5], obj.getStrongest( arr = [1,1,3,5,5], k = 2 ) )
print( [11,8,6,6,7], obj.getStrongest( arr = [6,7,11,7,6,8], k = 5 ) )
print( [-3,11,2], obj.getStrongest( arr = [6,-3,7,2,11], k = 3 ) )
print( [22,17], obj.getStrongest( arr = [-7,22,17,3], k = 2 ) )
print( [-1,-9,-2], obj.getStrongest( arr = [-2,-4,-6,-8,-9,-7,-5,-3,-1], k=3 ) )