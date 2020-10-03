from typing import List
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = ["" for _ in range(len(s))]
        for c, i in zip(s, indices):
            result[i] = c
        return "".join(result)

obj = Solution()
print(obj.restoreString(s = "codeleet", indices = [4,5,6,7,0,2,1,3]))