import numpy
class Solution:
    def minSubsequence(self, nums: [int]) -> [int]:
        nums.sort()
        old_sum = numpy.sum(nums)
        nums.reverse()

        result_list, new_sum = [], 0
        for num in nums: 
            result_list.append(num)
            
            new_sum += num
            old_sum -= num

            if new_sum > old_sum:
                return result_list



obj = Solution()

print( [10,9],  obj.minSubsequence( nums = [4,3,10,9,8] ) )
print( [7,7,6], obj.minSubsequence( nums = [4,4,7,6,7] ) )
print( [6],     obj.minSubsequence( nums = [6] ) )




