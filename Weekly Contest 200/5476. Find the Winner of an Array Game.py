from typing import List
class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        index, length, temp_counter = 0, len(arr), 0
        while index < length:
            lost, temp_winner = False, arr.pop(0)
            for i in range(len(arr)):
                if temp_counter >= k:
                    return temp_winner
                    
                if temp_winner > arr[i]: 
                    temp_counter += 1
                else:
                    temp_counter = 1
                    lost = True
                    break
            if lost:
                arr.append(temp_winner)
                index += 1
            else:
                return temp_winner

obj = Solution()
print(5, obj.getWinner( arr = [2,1,3,5,4,6,7], k = 2 ))
print(3, obj.getWinner( arr = [3,2,1] , k = 10 ))