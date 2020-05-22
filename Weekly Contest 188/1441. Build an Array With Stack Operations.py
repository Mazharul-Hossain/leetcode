from typing import List

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        return_list = []
        
        target_pointer = 0
        for i in range(1, n+1):            
            if target_pointer >= len(target):
                break

            if target[target_pointer] == i:
                target_pointer += 1
                return_list.append("Push")
            else:
                return_list.append("Push")
                return_list.append("Pop")
        return return_list


obj = Solution()

print( ["Push","Push","Pop","Push"],        obj.buildArray( target = [1,3], n = 3 ) )
print( ["Push","Push","Push"],              obj.buildArray( target = [1,2,3], n = 3 ) )
print( ["Push","Push"],                     obj.buildArray( target = [1,2], n = 4 ) )
print( ["Push","Pop","Push","Push","Push"], obj.buildArray( target = [2,3,4], n = 4 ) )