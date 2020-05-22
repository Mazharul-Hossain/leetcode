class Solution:
    def createTargetArray(self, nums: [int], index: [int]) -> [int]:
        output = []
        for indx, num in zip(index, nums):
            if indx > len(output):
                output.append(num)
            else:
                output = output[:indx] + [num] + output[indx:]
        return output



obj = Solution()

print([0,4,1,3,2], obj.createTargetArray( nums = [0,1,2,3,4], index = [0,1,2,2,1] ) )
print([0,1,2,3,4], obj.createTargetArray( nums = [1,2,3,4,0], index = [0,1,2,3,0] ) )