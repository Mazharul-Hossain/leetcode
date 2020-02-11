class Solution:
    def kWeakestRows(self, mat: [[int]], k: int) -> [int]:
        import numpy
        result = []

        for row in mat:
            result.append(numpy.sum(numpy.asarray(row)))
        # print(result)
        result = numpy.argsort(numpy.asarray(result))
        # print(result[:k])
        return result[:k]


# input 2
mat = [[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]]
k = 3
Solution().kWeakestRows(mat, k)

# input 2
mat = [[1,0,0,0],  [1,1,1,1], [1,0,0,0],  [1,0,0,0]]
k = 2
Solution().kWeakestRows(mat, k)