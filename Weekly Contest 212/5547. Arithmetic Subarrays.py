from typing import List


class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        answer = []
        for left, right in zip(l, r):
            target = nums[left: right + 1]
            target.sort()
            # print(target)

            arithmetic, flag = None, True
            for i in range(1, len(target)):
                if arithmetic is None:
                    arithmetic = target[i] - target[i - 1]
                else:
                    if arithmetic != target[i] - target[i - 1]:
                        flag = False
                        break
            answer.append(flag)
        return answer


obj = Solution()
print(obj.checkArithmeticSubarrays(nums=[4, 6, 5, 9, 3, 7], l=[0, 0, 2], r=[2, 3, 5]))
print(obj.checkArithmeticSubarrays(nums=[-12, -9, -3, -12, -6, 15, 20, -25, -20, -15, -10], l=[0, 1, 6, 4, 8, 7],
                                   r=[4, 4, 9, 7, 9, 10]))
