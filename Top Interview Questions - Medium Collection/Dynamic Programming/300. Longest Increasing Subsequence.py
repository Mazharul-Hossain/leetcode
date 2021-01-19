from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length = len(nums)
        if length <= 1:
            return length

        answer = [1 for _ in range(length)]
        for i in range(length - 2, -1, -1):
            for j in range(i + 1, length):
                if nums[j] > nums[i]:
                    # print(i, nums[i], j, nums[j])
                    answer[i] = max(answer[i], answer[j] + 1)
            # print(nums[i], answer[i])
        return max(answer)


obj = Solution()
print(4, obj.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
