class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        index, s = 0, "0"
        while index <= n:
            temp_s = s + "1"
            if len(temp_s) >= k:
                return temp_s[k-1]
            s = temp_s + s.translate(str.maketrans("10","01"))[::-1]
            index += 1

obj = Solution()
print( "0", obj.findKthBit( n = 3, k = 1))
print( "1", obj.findKthBit( n = 4, k = 11))
print( "0", obj.findKthBit( n = 1, k = 1))
print( "1", obj.findKthBit( n = 2, k = 3 ))
print( "0", obj.findKthBit( n = 3, k = 5 ))