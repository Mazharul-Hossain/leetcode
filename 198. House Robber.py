class Solution:
    def rob(self, nums: [int]) -> int:
        length = len(nums)
        if length == 0:
            return 0
        elif length == 1:
            return nums[0]
        elif length == 2:
            if nums[0] >= nums[1]:
                return nums[0]
            else:
                return nums[1]

        money_list = [nums[0], nums[1]]        
        for index_ in range(0, length - 2):
            for count_ in range(2, 4):
                index = index_ + count_
                if index >= length: 
                    break
                sum = money_list[index_] + nums[index]
                if index >= len(money_list):
                    money_list.append(sum)
                else:
                    if money_list[index] < sum:
                        money_list[index] = sum
        if money_list[length - 1] >= money_list[length - 2]:
            return money_list[length - 1]
        else:
            return money_list[length - 2]

nums = [1,2,3,1,2,7,9,3,1]
print(Solution().rob(nums))



