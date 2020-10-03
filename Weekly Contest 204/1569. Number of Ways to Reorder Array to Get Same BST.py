from scipy import special
from typing import List
class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        def f(nums):
            if len(nums) <= 2: return 1
            left = [v for v in nums if v < nums[0]]
            right = [v for v in nums if v > nums[0]]

            ans1 = special.comb( len(left)+len(right), len(right), exact=True ) 
            ans2 = f(left) 
            ans3 = f(right)
            # print( ans1, ans2, ans3)
            return ans1 * ans2 * ans3
        return (f(nums)-1) % (10**9+7)     


obj = Solution()
print(1, obj.numOfWays(nums = [2,1,3]))
print(5, obj.numOfWays( nums = [3,4,5,1,2]))
print(0, obj.numOfWays(nums = [1,2,3]))
print(19, obj.numOfWays(nums = [3,1,2,5,4,6]))
print(216212978, obj.numOfWays( nums = [9,4,2,1,3,6,5,7,8,14,11,10,12,13,16,15,17,18]))