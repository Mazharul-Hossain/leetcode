from typing import List
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        counter = 0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if abs(arr[i] - arr[j]) > a:
                    continue
                for k in range(j+1, len(arr)):
                    if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:                   
                        counter += 1
        return counter
                    
obj = Solution()
print(4, obj.countGoodTriplets( arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3 ) )