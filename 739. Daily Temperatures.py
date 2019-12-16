import operator

class Solution:
    def dailyTemperatures(self, T: [int]) -> [int]:
        length = len(T)
        output = [0 for i in range(length)]

        if length <= 1:
            return output
        # if(len(set(T))==1):
        #     return output
        # if T == sorted(T, reverse=True):
        #     return output
        
        input = {}
        max_value = max(T)
        # print(max_value)
        un_sort_flag = False
        for i in range(length - 2, -1, -1):             
            # print(i, T[i + 1], T[i])
            if T[i + 1] > T[i]:
                output[i] = 1
                un_sort_flag = True
            else:
                if T[i] == max_value:
                    continue
                if un_sort_flag:
                    input[i] = T[i]
        # print(input, output)    
        
        # print("starting: ", T)        
        # max_value = max(input.items(), key=operator.itemgetter(1))[1]            
        # for key, value in input.items():
        # for counter in range(1, length):
        #     if len(input) <= 0: 
        #         break
        for key in input.copy():
            # print(key,"#working for: ", T[key])
            for counter in range(1, length):
                current_distance = counter + output[key + 1]
                if length <= (key + current_distance):
                    # print("removing: ", T[key])
                    input.pop(key)
                    break
                # length > (key + counter)
                elif T[key + current_distance] > T[key]:
                    # print("removing: ", T[key], output[key])
                    output[key] = current_distance 
                    input.pop(key)
                    break                                    
        return output

T = [73,74,75,71,69,72,76,73]
ret = Solution().dailyTemperatures(T)
# print(", ".join(str(v) for v in ret))
print(T, ret)

T = [76, 75, 74, 73, 73, 72, 71, 69]
ret = Solution().dailyTemperatures(T)
print(T, ret)

T = [ 71, 71, 71, 71, 76, 71, 71, 71]
ret = Solution().dailyTemperatures(T)
print(T, ret)

T = [64,40,49,73,72,35,68,83,35,73,84,88,96,43,74,63,41]
ret = Solution().dailyTemperatures(T)
print(T, ret)
