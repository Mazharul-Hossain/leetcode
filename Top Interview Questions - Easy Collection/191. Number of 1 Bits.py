class Solution:
    def hammingWeight(self, n: int) -> int:
        counter = 0
        while n != 0:
            if n%2 == 1:
                counter += 1
            n = n // 2
        return counter

obj = Solution()
print(obj.hammingWeight(n=11))