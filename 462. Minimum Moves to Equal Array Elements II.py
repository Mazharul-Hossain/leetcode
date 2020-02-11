class Solution:
    def minMoves2(self, nums: [int]) -> int:
        #==== not a mode problem ======#
        # import collections

        # # Print the list
        # # print(nums)

        # # calculate the frequency of each item
        # data = collections.Counter(nums)
        # data_list = dict(data)

        # # Print the items with frequency
        # # print(data_list)

        # # Find the highest frequency
        # max_value = max(list(data.values()))

        # return len(nums) - max_value

        #==== but a median problem ======#
        nums.sort()
        median = nums[len(nums) // 2]
        # print("median: ",median)

        result_sum = 0
        for num in nums:
            result_sum += abs(num - median) 
        return result_sum

        # https://railsware.com/blog/python-for-machine-learning-indexing-and-slicing-for-lists-tuples-strings-and-other-sequential-types/
        # https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/discuss/94923/2-lines-Python-2-ways
        print(nums)
        for i in range(len(nums) // 2):
            print(nums[~i], nums[i]) 
        return sum(nums[~i] - nums[i] for i in range(len(nums) // 2))

        
            


print(Solution().minMoves2([1,2,3]))
print(Solution().minMoves2([21, 13, 19, 13,19,13]))