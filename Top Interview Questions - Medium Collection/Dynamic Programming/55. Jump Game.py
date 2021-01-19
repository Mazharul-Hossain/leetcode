from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        length, goal = len(nums) - 1, len(nums) - 2
        for i in range(length, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        if goal > 0:
            return False
        else:
            return True


obj = Solution()
print(obj.canJump(nums=[2, 3, 1, 1, 4]))
print(obj.canJump(nums=[3, 2, 1, 0, 4]))
