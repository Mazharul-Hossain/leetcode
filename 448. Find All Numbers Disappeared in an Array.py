class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # https://www.geeksforgeeks.org/python-list-sort/
        return_list = []
        if nums:
            nums.sort()
            head = 1
            if nums[0] > head:
                for j in range(head, nums[0]):
                    return_list.append(j)
            head = nums[0] + 1
            length = len(nums)    
            for i in range(1, length):
                if nums[i] == nums[i - 1]:
                    continue
                if nums[i] > head:
                    for j in range(head, nums[i]):
                        return_list.append(j)
                head = nums[i] + 1
            if length >= head:
                    for j in range(head, length + 1):
                        return_list.append(j)
        return return_list