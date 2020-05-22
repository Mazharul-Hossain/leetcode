from typing import List
import numpy

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix_shape = numpy.asarray(matrix).shape
        
        # check if first row will be zeros, now use it
        first_row_zero = False        
        for row in range( matrix_shape[0] ):
            if row >= 1:
                break
            for column in range( matrix_shape[1] ):
                if matrix[row][column] == 0:
                    first_row_zero =True
                    break         
        # now checked, use first row as flag for all other columns
        for column in range(matrix_shape[1] ):
            for row in range(1, matrix_shape[0] ):
                if matrix[row][column] == 0:
                    # saving column flag
                    matrix[0][column] = 0
                    # saving row flag
                    matrix[row][0] = 0
        
        # use first column, to mark all other rows 
        for row in range(1, matrix_shape[0] ):
            if matrix[row][0] == 0:
                for column in range(1, matrix_shape[1] ):
                    matrix[row][column] = 0

        # use first row, to mark all other columns
        for column in range(matrix_shape[1] ):
            if matrix[0][column] == 0:
                for row in range(1, matrix_shape[0] ):
                    matrix[row][column] = 0
        
        # update first row with zero
        if first_row_zero:
            for column in range( matrix_shape[1] ):
                matrix[0][column] = 0

        return matrix


obj = Solution()
print( obj.setZeroes( matrix = [ [1,1,1], [1,0,1], [1,1,1] ] ) )