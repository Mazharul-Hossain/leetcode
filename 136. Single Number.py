import collections
class Solution:
    def singleNumber(self, nums) -> int:
        # # https://stackoverflow.com/q/473099/2049763
        # solution_list = collections.defaultdict(int)
        # for num in nums:
        #     if num in solution_list:
        #         solution_list[num] += 1
        #     else:
        #         solution_list[num] = 1
        # for key, value in solution_list.items():
        #     # https://stackoverflow.com/a/3294899/2049763
        #     if value == 1:
        #         return key
        nums.sort()
        length = len(nums) - 1
        for i in range(0, length, 2):        
            if(nums[i] != nums[i+1]):
                return nums[i] 
        return nums[length]