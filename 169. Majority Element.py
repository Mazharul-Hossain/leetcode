class Solution:
    def majorityElement(self, nums):
        nums.sort()
        count, pointer = 1, nums[0]
        length = len(nums) 
        for i in range(1,length):
            if count > length/2 :
                break
            if pointer == nums[i]:
                count += 1
            else:
                pointer = nums[i]
                count = 1
        return pointer


sol = Solution()
print(sol.majorityElement([3,2,3]))
print(sol.majorityElement([2,2,1,1,1,2,2]))