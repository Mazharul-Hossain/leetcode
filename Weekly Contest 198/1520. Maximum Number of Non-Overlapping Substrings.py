from typing import List 
class Solution:
    def checkSubstr(self, s: str, i: int, r: List[int], l: List[int]):
        right = r[ord(s[i]) - ord('a')]
        for j in range(i, right + 1):
            if l[ord(s[j]) - ord('a')] < i:
                return -1
            right = max(right, r[ord(s[j]) - ord('a')])
        return right

    def maxNumOfSubstrings(self, s: str) -> List[str]:
        # https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/discuss/743223/C%2B%2BJava-Greedy-O(n)
        l, r = [float('inf')]*26, [float('-inf')]*26
        result = []
        for i in range(len(s)):
            point = ord(s[i]) - ord('a') 
            l[point] = min(l[point], i)
            r[point] = max(r[point], i)

        right = float('-inf')
        for i in range(len(s)):
            if (i == l[ord(s[i]) - ord('a')]):
                new_right = self.checkSubstr(s, i, l, r)
                if (new_right != -1):
                    if (i > right):
                        result.append("")                     
                    right = new_right
                    result[-1] = s[i : right + 1]
        return result


obj = Solution()
print( ["e","f","ccc"], obj.maxNumOfSubstrings( s = "adefaddaccc" ) )
# prord( ["d","bb","cc"], obj.maxNumOfSubstrings( s = "abbaccd" ) )