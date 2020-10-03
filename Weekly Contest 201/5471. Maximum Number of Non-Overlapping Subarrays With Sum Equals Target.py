from typing import List

class Solution:
    # https://leetcode.com/problems/maximum-number-of-non-overlapping-subarrays-with-sum-equals-target/discuss/780887/Java-Detailed-Explanation-DPMapPrefix-O(N)
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        map = {0: 0}
        ans, sum = 0, 0

        for i in range(len(nums)):
            sum += nums[i]
            if (sum - target) in map: 
                ans = max(ans, map[sum - target] + 1)
            map[sum] = ans
        return ans

obj = Solution()
print( 2, obj.maxNonOverlapping( nums = [1,1,1,1,1], target = 2 ))
print( 2, obj.maxNonOverlapping( nums = [-1,3,5,1,4,2,-9], target = 6))
print( 3, obj.maxNonOverlapping( nums = [-2,6,6,3,5,4,1,2,8], target = 10 ))
print( 3, obj.maxNonOverlapping( nums = [0,0,0], target = 0 ))