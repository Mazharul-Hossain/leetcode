from typing import List


class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        if not nums:
            return 0
        sums = [nums[0]]
        for i in range(1, len(nums)):
            sums.append(sums[i - 1] + nums[i])

        counter, length = 0, len(nums)
        for left in range(length - 2):
            for right in range(left + 1, length - 1):
                sum_left, sum_mid, sum_right = sums[left], sums[right] - sums[left], sums[length - 1] - sums[right]
                print(sum_left, sum_mid, sum_right)
                if sum_mid > sum_right:
                    break
                if sum_left <= sum_mid <= sum_right:
                    counter += 1
        return counter


obj = Solution()
print(obj.waysToSplit(nums=[1, 1, 1]))
print(obj.waysToSplit(nums=[1, 2, 2, 2, 5, 0]))
print(obj.waysToSplit(nums=[3, 2, 1]))
