class Solution:
    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left+1, right-1

    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        for i in range( len(s) - 1):
            left, right = self.expandAroundCenter(s, i, i)
            if right - left > end - start:
                start, end = left, right

            left, right = self.expandAroundCenter(s, i, i+1)
            if right - left > end - start:
                start, end = left, right
        return s[start: end+1]


obj = Solution()
print( obj.longestPalindrome( "babad" ) )
print( obj.longestPalindrome( "cbbd" ) )