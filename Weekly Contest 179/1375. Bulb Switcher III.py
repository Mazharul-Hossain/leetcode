class Solution:
    def numTimesAllBlue(self, light: [int]) -> int:
        # length = len(light)

        # if all(light[i] < light[i+1] for i in range( length-2) ):
        #     return length


        # result_light = [1 for i in range(length)]

        # counter = 0
        # for i in range(length-1, -1, -1):
        #     if result_light[i] == 1:
        #         counter += 1 
        #         for j in range(i, -1, -1):
        #             if light[j] > light[i]:
        #                 result_light[j] = 0        
        # return counter
        
        res,cur_max = 0, 0
        for index, bulb in enumerate(light):
            cur_max = max(bulb, cur_max)
            if cur_max == index+1:  
                res += 1
        return res


obj = Solution()
print(obj.numTimesAllBlue( [1,2,3] ))
print("3", obj.numTimesAllBlue( [2,1,3,5,4] ))
print("2", obj.numTimesAllBlue( [3,2,4,1,5] ))
print("1", obj.numTimesAllBlue( [4,1,2,3] ))
print("3", obj.numTimesAllBlue( [2,1,4,3,6,5] ))
print("6", obj.numTimesAllBlue( [1,2,3,4,5,6] ))


