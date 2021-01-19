from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        prefix_sum = []

        def get_sum(left, right):
            if not prefix_sum:
                for num in nums:
                    if len(prefix_sum) == 0:
                        prefix_sum.append(num)
                    else:
                        prefix_sum.append(num + prefix_sum[-1])
                # print(nums, prefix_sum)
            if left == 0:
                return prefix_sum[right]
            else:
                return prefix_sum[right] - prefix_sum[left - 1]

        max_sum, current, index_map = 0, 0, {}
        for i, num in enumerate(nums):
            if num in index_map:
                # print("index_map: ", current, index_map[num])
                if current <= index_map[num]:
                    current = index_map[num] + 1
            index_map[num] = i

            temp_sum = get_sum(current, i)
            # print(current, i, temp_sum)
            if temp_sum > max_sum:
                max_sum = temp_sum
        return max_sum


obj = Solution()
print(17, obj.maximumUniqueSubarray(nums=[4, 2, 4, 5, 6]))
print(8, obj.maximumUniqueSubarray(nums=[5, 2, 1, 2, 5, 2, 1, 2, 5]))
print(16911, obj.maximumUniqueSubarray(
    nums=[187, 470, 25, 436, 538, 809, 441, 167, 477, 110, 275, 133, 666, 345, 411, 459, 490, 266, 987, 965,
          429, 166, 809, 340, 467, 318, 125, 165, 809, 610, 31, 585, 970, 306, 42, 189, 169, 743, 78, 810,
          70, 382, 367, 490, 787, 670, 476, 278, 775, 673, 299, 19, 893, 817, 971, 458, 409, 886, 434]))
