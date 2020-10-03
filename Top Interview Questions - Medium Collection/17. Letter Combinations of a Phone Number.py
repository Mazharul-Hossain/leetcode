from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        if digits is None or len(digits) == 0:
            return result
        
        mapping = ["0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        result.append("")

        while len(result[0]) < len(digits):
            remove = result.pop(0)
            index = len(remove)
            index = ord(digits[index]) - ord('0')
            for c in mapping[index]:
                result.append(remove+c)
        return result

obj = Solution()
print(obj.letterCombinations( digits="23" ) )