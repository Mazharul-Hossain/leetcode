from typing import List
import math 

class Solution:
    # https://leetcode.com/problems/best-position-for-a-service-centre/discuss/731577/C%2B%2B-with-picture-zoom-in
    # def getMinDistSum(self, positions: List[List[int]]) -> float:
    #     left, right, bottom, top = 0.0, 100.0, 0.0, 100.0
    #     for position in positions:
    #         x, y = position
    #         left, right = min(left, x),   max(right, x)
    #         bottom, top = min(bottom, y), max(top, y)

    # Weiszfeld's algorithm: https://en.wikipedia.org/wiki/Geometric_median
    # https://leetcode.com/problems/best-position-for-a-service-centre/discuss/731599/Weiszfeld's-algorithm
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        n = len(positions)
        if n == 1: return 0.0
        preans = float('inf')
        ans = 0
        
        # Use mean point as the initial point
        x, y = [sum(i) for i in zip(*positions)]
        
        def distancesum(x, y):
            temp = 0
            for a, b in positions:
                temp += math.sqrt(abs(x - a) ** 2 + abs(y - b) ** 2)
            return temp
        
        def bottomsum(x, y):
            res = 0
            for a, b in positions:
                temp = math.sqrt(abs(x - a) ** 2 + abs(y - b) ** 2)
                # Handle 0 exception
                if temp == 0: continue
                res += 1 / temp 
            return res
        
        def uppersum(x, y):
            xx = 0
            yy = 0
            for a, b in positions:
                temp = math.sqrt(abs(x - a) ** 2 + abs(y - b) ** 2)
                # Handle 0 exception
                if temp == 0: continue
                xx += a / temp
                yy += b / temp
            return (xx, yy)
        
        def weis(x, y):
            xx, yy = uppersum(x, y)
            bottom = bottomsum(x, y)
            # Handle 0 exception
            if bottom == 0:
                return (x, y)
            return (xx / bottom, yy / bottom)
        
        # Iterate Weiszfeld until the improvement is insignificant
        while abs(ans - preans) > 1e-7:
            preans = ans
            x, y = weis(x, y)
            ans = distancesum(x, y)
        
        return ans