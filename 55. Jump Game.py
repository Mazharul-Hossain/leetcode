class Solution:
    def canJump(self, nums: [int]) -> bool:
        # index = nums[0]
        # while(index < len(nums)):
        #     jump = index + nums[index]
        #     if jump == ( len(nums) -1 ) :
        #         return True
        #     if jump == index:
        #         return False
        #     index = jump
        # return True

        # length = len(nums)
        # jump_list = [False for x in range(length)]

        # jump_list[length - 1] = True
        # for index in range(length - 2, -1, -1 ):
        #     if index + nums[index] >= length - 1:
        #         jump_list[index] = True
        #     else:
        #         for index_1 in range(nums[index], 0, -1 ):
        #             if jump_list[index + index_1]:
        #                 jump_list[index] = True
        #                 break
        # return jump_list[0]

        # https://leetcode.com/problems/jump-game/discuss/20907/1-6-lines-O(n)-time-O(1)-space
        length = len(nums)
        goal = length - 1
        for index in range(length - 2, -1, -1 ):
            if index + nums[index] >= goal:
                goal = index
        if goal >= 1 :
            return False
        else : 
            return True 

nums = [2,3,1,1,4]
print(Solution().canJump(nums))

nums = [3,2,1,0,4]
print(Solution().canJump(nums))

nums = [0]
print(Solution().canJump(nums))

nums = [2,5,0,0]
print(Solution().canJump(nums))