from typing import List
class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        length = [0] * (len(arr) + 2)
        count = [0] * (len(arr) + 1)
        res = -1
        for i, a in enumerate(arr):
            left, right = length[a - 1], length[a + 1]
            length[a] = length[a - left] = length[a + right] = left + right + 1
            # print(a, left, right, length[a], length[a - left], length[a + right])
            count[left] -= 1
            count[right] -= 1
            count[length[a]] += 1
            if count[m]:
                res = i + 1
            print(length, count, res)
        return res

obj = Solution()
# print(obj.findLatestStep( arr = [3,5,1,2,4], m = 1 ))
print(obj.findLatestStep( arr = [3,1,5,4,2], m = 2 ))
# print(obj.findLatestStep( arr = [1], m = 1 ))
# print(obj.findLatestStep( arr = [2,1], m = 2 ))