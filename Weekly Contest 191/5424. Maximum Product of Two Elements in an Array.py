from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-1] - 1) * (nums[-2] - 1)

obj = Solution()
print( 12, obj.maxProduct( nums = [3,4,5,2] ) )
print( 16, obj.maxProduct( nums = [1,5,4,5] ) )
print( 12, obj.maxProduct( nums = [3,7] ) )