class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        head = 0        
        while count < len(nums):
            if nums[count] is 0:
                count += 1
            else:
                if head != count:
                    nums[head] = nums[count]
                    nums[count] = 0
                head, count = head + 1, count + 1
