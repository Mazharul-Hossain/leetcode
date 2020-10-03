import operator as op
from functools import reduce

class Solution:    
    def ncr(self, n, r):
        # https://stackoverflow.com/a/4941932/2049763
        r = min(r, n-r)
        numer = reduce(op.mul, range(n, n-r, -1), 1)
        denom = reduce(op.mul, range(1, r+1), 1)
        return numer // denom  # or / in Python 2

    def substring(self, counter):
        result = 0
        for i in range(counter):
            for _ in range(i + 1, counter + 1):
                result += 1
        return result

    def countSubString(self, counter):
        print("called:", counter)
        return counter * ( counter + 1 ) // 2
        # if counter > 1:
        #     return ( counter*(counter+1) ) // 2
        # else:
        #     return counter
    
    def numSub(self, s: str) -> int:
        result, counter = 0, 0
        s = s.split('0') 
        for c in s:
            counter = len(c)
            result = ( result + counter * ( counter + 1 ) // 2 ) % (10**9 + 7)
        return result

obj = Solution()
print( 9, obj.numSub( s = "0110111"))
print( 2, obj.numSub( s = "101"))
print( 21, obj.numSub( s = "111111"))
print( 0, obj.numSub( s = "000"))
print( 0, obj.numSub( s = "111000101010111100000111111111111" ))