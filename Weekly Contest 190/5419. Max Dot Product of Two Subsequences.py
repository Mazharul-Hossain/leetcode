from typing import List
class Solution:    
    # Longest Common Subsequence Problem
    # https://leetcode.com/problems/max-dot-product-of-two-subsequences/discuss/648420/JavaC%2B%2BPython-the-Longest-Common-Sequence
    # recursion with memoization
    # def maxDotProduct(self, A: List[int], B: List[int], a: int=None, b: int=None, hash_map=None) -> int:        
    #     if a is None:
    #         a = len(A) - 1
    #     if b is None: 
    #         b = len(B) - 1
    #     if hash_map is None:
    #         hash_map = {}

    #     if (a,b) not in hash_map:
    #         dot_product = A[a] * B[b]
    #         if a > 0 and b > 0:
    #             dot_product += max( 0, self.maxDotProduct(A, B, a-1, b-1, hash_map) )

    #         if a > 0:
    #             dot_product = max( dot_product, self.maxDotProduct(A, B, a-1, b, hash_map) )

    #         if b > 0:
    #             dot_product = max( dot_product, self.maxDotProduct(A, B, a, b-1, hash_map) )

    #         hash_map[(a,b)] = dot_product
    #     return hash_map[(a,b)]
    # #######################################################
    # Dynamic programming
    def maxDotProduct(self, A: List[int], B: List[int]) -> int:
        a, b, dp = len(A), len(B), []
        
        for i in range(a):
            dp.append([])
        
            for j in range(b):
                dp[i].append( A[i] * B[j] )
                
                if i > 0 and j > 0:
                    dp[i][j] += max( 0, dp[i-1][j-1] )
                if i > 0:
                    dp[i][j] = max( dp[i][j], dp[i-1][j] )
                if j > 0:
                    dp[i][j] = max( dp[i][j], dp[i][j-1] )
        return dp [-1][-1]


obj = Solution()
print( 18, obj.maxDotProduct( A = [2,1,-2,5], B = [3,0,-6] ) )
print( 21, obj.maxDotProduct( A = [3,-2], B = [2,-6,7] ) )
print( -1, obj.maxDotProduct( A = [-1,-1], B = [1,1] ) )