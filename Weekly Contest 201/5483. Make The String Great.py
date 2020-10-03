class Solution:
    def makeGood(self, s: str) -> str:
        i = 0
        while i <= len(s) - 2:
            if abs(ord(s[i]) - ord(s[i+1])) == 32:
                s = s.replace(s[i:i+2], '', 1)
                
                if i > 0:
                    i -= 1 
            else:
                i += 1
        return s

obj = Solution()
print( "leetcode", obj.makeGood( s = "leEeetcode"))
print( "", obj.makeGood( s = "abBAcC"))
print( "s", obj.makeGood( s = "s"))