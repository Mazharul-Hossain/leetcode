class Solution:
    def luckyNumbers (self, matrix: [[int]]) -> [int]:

        import numpy as np

        for i in range( len( matrix) ):
            row = matrix[i] 
            index = np.argmin(row)

            flag = True
            for j in range( len( matrix) ):
                if i == j :
                    continue
                if matrix[j][index] > matrix[i][index]:
                    flag = False
                    break
            if flag: 
                return [ row[index] ]



obj = Solution()
print( [15], obj.luckyNumbers( [[3,7,8],[9,11,13],[15,16,17]] ) )     
print( [12], obj.luckyNumbers( [[1,10,4,2],[9,3,8,7],[15,16,17,12]] ) )  
print( [7], obj.luckyNumbers( [[7,8],[1,2]] ) )       