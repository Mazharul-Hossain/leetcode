from typing import List

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        dict = {}
        for a in arr:
            if a not in dict:
                dict[a] = 0
            dict[a] += 1
        dict = { key: value for key, value in sorted(dict.items(), key=lambda item: item[1]) }

        remove_list = []
        for key, value in dict.items():
            if k <= 0:
                break
            if k < value:
                dict[key] = value - k
            else:
                k -= value 
                remove_list.append(key)

        for key in remove_list:
            del dict[key]
        return len(dict)

obj = Solution()
print( 1, obj.findLeastNumOfUniqueInts( arr = [5,5,4], k = 1 ) )
print( 2, obj.findLeastNumOfUniqueInts( arr = [4,3,1,1,3,3,2], k = 3 ) )
print( 4, obj.findLeastNumOfUniqueInts( arr = [9,17,11,19,4,22,27,15,24,30,45,11,17,37,37], k=8) ) 