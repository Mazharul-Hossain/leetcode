from typing import List
class Solution:
    def generateParenthesis(self, n: int, result: List[str]=None, s: str="", open: int=0, close: int=0) -> List[str]:
        if result is None:
            result = []
        if len(s) == 2*n:
            result.append(s)
            return result

        if open < n :
            result = self.generateParenthesis(n, result, s+"(", open+1, close)
        if close < open :
            result = self.generateParenthesis(n, result, s+")", open, close+1)
        return result
        
obj = Solution()
print(obj.generateParenthesis(n=2))
print(obj.generateParenthesis(n=3))
print(obj.generateParenthesis(n=4))
print(obj.generateParenthesis(n=1))
print(obj.generateParenthesis(n=0))