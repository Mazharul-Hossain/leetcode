from typing import List
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums) ):
            nums[i] += nums[i-1]

        return nums


obj = Solution()
print( [1,3,6,10], obj.runningSum( nums = [1,2,3,4] ) )
print( [1,2,3,4,5], obj.runningSum( nums = [1,1,1,1,1] ) )
print( [3,4,6,16,17], obj.runningSum( nums = [3,1,2,10,1] ) )