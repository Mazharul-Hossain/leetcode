class Solution:
    def smallerNumbersThanCurrent(self, nums: [int]) -> [int]:
        result = [0 for i in nums]

        import numpy
        sorted_nums = numpy.argsort(numpy.asarray(nums)) 

        for i in range( 1, len(sorted_nums) ):
            if nums[ sorted_nums[i] ] == nums[ sorted_nums[i-1] ]:
                result[ sorted_nums[i] ] = result[ sorted_nums[i-1] ]
            else:
                result[ sorted_nums[i] ] = i

        return result


obj = Solution()
print([4,0,1,1,3], obj.smallerNumbersThanCurrent([8,1,2,2,3] ) )
print([2,1,0,3],   obj.smallerNumbersThanCurrent([6,5,4,8]   ) )
print([0,0,0,0],   obj.smallerNumbersThanCurrent([7,7,7,7]   ) )  