class Solution:
    def circularPermutation(self, n: int, start: int) -> [int]:
        # https://leetcode.com/problems/circular-permutation-in-binary-representation/discuss/414147/Python-recursion
        result = self.nBitsGrayCodes(n)
        result = [int(x, 2) for x in result]

        index = result.index(start)
        return result[index:] + result[:index] 

    def nBitsGrayCodes(self, n: int) -> [int]:
        # https://leetcode.com/problems/circular-permutation-in-binary-representation/discuss/414153/Java-AC-solution%3A-generate-%22one-bit-diff%22-list-then-make-it-start-from-%22start%22
        if n <= 0:
            return []
        
        grey_lis_1 = ["0", "1"]
        for i in range(1, n):
            grey_lis_2 = grey_lis_1[::-1]
            grey_lis_1 = ["0"+ x for x in grey_lis_1] 
            grey_lis_2 = ["1"+ x for x in grey_lis_2]

            grey_lis_1.extend(grey_lis_2)
        return grey_lis_1

result = Solution().nBitsGrayCodes(2)
print(result)
result = [int(x, 2) for x in result]
print(result)

print(Solution().circularPermutation(2, 3))
print(Solution().circularPermutation(3, 2))