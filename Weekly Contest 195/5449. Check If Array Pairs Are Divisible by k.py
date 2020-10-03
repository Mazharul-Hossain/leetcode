from typing import List
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        result = {}
        for a in arr:
            t = a % k
            print(t, result)
            if t in result:
                result[t] -= 1
                if result[t] == 0:
                    del result[t]
            else:
                if t != 0:
                    t = k - t
                if t not in result:
                    result[t] = 0
                result[t] += 1
        if len(result) == 0:
            return True
        return False

obj = Solution()
print(obj.canArrange(arr = [1,2,3,4,5,10,6,7,8,9], k = 5))