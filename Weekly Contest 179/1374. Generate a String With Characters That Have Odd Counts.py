class Solution:
    def generateTheString(self, n: int) -> str:
        str_list = ["a", "b", "c", "d"]

        if n%2:
            return str_list[0] * n
        else:
            return str_list[0] * (n-1) + str_list[1]


obj = Solution()
print(obj.generateTheString(4))
print(obj.generateTheString(2))
print(obj.generateTheString(7))