class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        n = x ^ y
        counter = 0
        while n != 0:
            if n%2 == 1:
                counter += 1
            n = n // 2
        return counter

obj = Solution()
print(obj.hammingDistance(x = 1, y = 4))