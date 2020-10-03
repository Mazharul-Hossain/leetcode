class Solution:
    def minOperations(self, n: int) -> int:
        new_n = (n-1) // 2
        if n%2==1:
            counter = 0
            median = (2 * new_n) + 1
        else:
            counter = 1            
            median = (2 * new_n) + 2 
        for i in range(new_n):
            a = (2 * i) + 1
            counter += (median - a)
        return counter

obj = Solution()
print( 2, obj.minOperations(3 ) )
print( 9, obj.minOperations(6) ) 