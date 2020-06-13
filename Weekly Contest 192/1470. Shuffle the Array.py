from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result_array, length = [], len(nums)

        for i in range(n):
            result_array.append(nums[i])
            result_array.append(nums[n+i])
        return result_array

obj = Solution()
print( [2,3,5,4,1,7], obj.shuffle( nums = [2,5,1,3,4,7], n = 3 ) )
print( [1,4,2,3,3,2,4,1], obj.shuffle( nums = [1,2,3,4,4,3,2,1], n = 4 ) )
print( [1,2,1,2], obj.shuffle( nums = [1,1,2,2], n = 2 ) )