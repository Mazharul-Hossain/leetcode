from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # https://youtu.be/qJSPYnS35SE
        nums.sort()
        output_array = []

        for i in range(len(nums) - 2):
            if i>0 and nums[i-1] == nums[i]:
                continue
            low, high = i+1, len(nums) - 1
            sum = 0 - nums[i]

            while (low < high):
                if (nums[low] + nums[high]) == sum:
                    output_array.append( [ nums[i], nums[low], nums[high] ] )
                    
                    while (low < high) and nums[low] == nums[low+1]:
                        low += 1
                    while (low < high) and nums[high-1] == nums[high]:
                        high -= 1
                
                    low += 1
                    high -= 1
                elif (nums[low] + nums[high]) > sum:
                    high -= 1
                else:
                    low += 1

        return output_array

obj = Solution()

print( obj.threeSum( nums = [-1, 0, 1, 2, -1, -4] ) )
print( obj.threeSum( nums = [0,0,0,0,0,0,0,0,0] ) )