import numpy
class Solution:
    # def maxSubArray(self, nums: List[int]) -> int:
    #     # O(n^2) solution
    #     new_sums = numpy.ndarray(shape=(len(nums), len(nums)), dtype=int) 
    #     max_sum = nums[0]              
    #     new_sums[0][0] = nums[0]
    #     for i in range(1, len(nums)):
    #         if nums[i] > max_sum:
    #             max_sum = nums[i]              
    #         new_sums[i][0] = nums[i]
    #         for j in range(i):
    #             sums = new_sums[i][0] + new_sums[i-1][j]
    #             if sums > max_sum:
    #                 max_sum = sums
    #             new_sums[i][j+1] =  sums
    #     return max_sum

    # def maxSubArray(self, nums: List[int]) -> int:
    #     # O(n) solution: greedy algo high memory
    #     new_sums = [nums[0]]
    #     for n in nums[1:]:
    #         new_sums.append( max( new_sums[-1] + n, n ) )
    #     return max(new_sums)

    def maxSubArray(self, nums: List[int]) -> int:
        # O(n) solution: greedy algo low memory
        max_sum, current_sum = nums[0], nums[0]
        for n in nums[1:]:
            current_sum = max( current_sum + n, n )
            max_sum = max( current_sum, max_sum )
        return max_sum

