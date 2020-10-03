import collections
import operator as op
from functools import reduce
from typing import List

class Solution:    
    def ncr(self, n, r):
        # https://stackoverflow.com/a/4941932/2049763
        r = min(r, n-r)
        numer = reduce(op.mul, range(n, n-r, -1), 1)
        denom = reduce(op.mul, range(1, r+1), 1)
        return numer // denom  # or / in Python 2


    def numIdenticalPairs(self, nums: List[int]) -> int:
        nums.sort()
        ctr = collections.Counter(nums)
        counter = 0
        for key, value in ctr.items():
            if value > 1:
                counter += self.ncr(value, 2)
        return counter


obj = Solution()
print( 4, obj.numIdenticalPairs( nums = [1,2,3,1,1,3] ) )
print( 6, obj.numIdenticalPairs( nums = [1,1,1,1]) )
print( 0, obj.numIdenticalPairs( nums = [1,2,3]) )