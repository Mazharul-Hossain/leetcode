from typing import List

class Solution:
    def inCircle(self, point: List[int]) -> bool:
        # https://stackoverflow.com/a/7227057/2049763
        dx = abs(point[0])
        if dx > self.r:
            return False
        dy = abs(point[1])
        if dy > self.r:
            return False
        if dx + dy <= self.r:
            return True
        return dx*dx + dy*dy <= self.r_2


    def numPoints(self, points: List[List[int]], r: int) -> int:
        counter = 0
        self.r = r
        self.r_2 = r * r
        for point in points:
            if self.inCircle(point):
                counter += 1
        return counter

obj = Solution()

print( 4, obj.numPoints( points = [[-2,0],[2,0],[0,2],[0,-2]], r = 2 ) )
print( 5, obj.numPoints( points = [[-3,0],[3,0],[2,6],[5,4],[0,9],[7,8]], r = 5 ) )
print( 1, obj.numPoints( points = [[-2,0],[2,0],[0,2],[0,-2]], r = 1 ) )
print( 4, obj.numPoints( points = [[1,2],[3,5],[1,-1],[2,3],[4,1],[1,3]], r = 2 ) )