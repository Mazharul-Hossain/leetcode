from typing import List

import numpy


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        special = 0
        mat = numpy.array(mat)
        col_sum = mat.sum(axis=0)
        row_sum = mat.sum(axis=1)

        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] == col_sum[j] == row_sum[i] == 1:
                    special += 1
        return special


obj = Solution()
print(1, obj.numSpecial(mat=[[1, 0, 0],
                             [0, 0, 1],
                             [1, 0, 0]]))
print(3, obj.numSpecial(mat=[[1, 0, 0],
                             [0, 1, 0],
                             [0, 0, 1]]))
print(2, obj.numSpecial(mat=[[0, 0, 0, 1],
                             [1, 0, 0, 0],
                             [0, 1, 1, 0],
                             [0, 0, 0, 0]]))
print(3, obj.numSpecial(mat=[[0, 0, 0, 0, 0],
                             [1, 0, 0, 0, 0],
                             [0, 1, 0, 0, 0],
                             [0, 0, 1, 0, 0],
                             [0, 0, 0, 1, 1]]))
print(2, obj.numSpecial(mat=[[0, 0, 1, 0],
                             [0, 0, 0, 0],
                             [0, 0, 0, 0],
                             [0, 1, 0, 0]]))
