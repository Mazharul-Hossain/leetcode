import sys
from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # https://leetcode.com/problems/increasing-triplet-subsequence/discuss/79004/Concise-Java-solution-with-comments.
        small, medium = sys.maxsize, sys.maxsize
        result_list = []
        
        for n in nums:
            if n <= small:
                small = n
            elif n <= medium:
                medium = n
                result_list = [small, medium]
            else:
                print( result_list[0], result_list[1], n )
                return True
        return False

obj = Solution()
print( True, obj.increasingTriplet( nums=[1,2,3,4,5] ) )
print( False, obj.increasingTriplet( nums=[5,4,3,2,1] ) )
print( True, obj.increasingTriplet( nums=[8,7,6,7,5,8] ) )
print( True, obj.increasingTriplet( nums=[1,0,2,0,-1,3] ) )