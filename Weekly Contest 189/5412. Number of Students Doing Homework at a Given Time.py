from typing import List

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        counter = 0

        for start, end in zip(startTime, endTime):
            if start <= queryTime and queryTime <= end:
                counter += 1
        return counter

obj = Solution()

print( obj.busyStudent( startTime = [1,2,3], endTime = [3,2,7], queryTime = 4 ) )
print( obj.busyStudent( startTime = [4], endTime = [4], queryTime = 4 ) )
print( obj.busyStudent( startTime = [4], endTime = [4], queryTime = 5 ) )
print( obj.busyStudent( startTime = [1,1,1,1], endTime = [1,3,2,4], queryTime = 7 ) )
print( obj.busyStudent( startTime = [9,8,7,6,5,4,3,2,1], endTime = [10,10,10,10,10,10,10,10,10], queryTime = 5 ) )