import numpy    

class Solution:
    # def __init__(self):
    #     self.comb = numpy.zeros(shape=(1000, 500))

    # def ncr(self, n, r):
    #     result = n
    #     for i in range(2, r+1):
    #         n = n - 1
    #         result *= n
            
    #         result /= i
    #     return int(result)

    # def get_ncr(self, n, r):
    #     r = min(r, n-r)
    #     if n < len(self.comb) and r < len(self.comb[0]):
    #         if self.comb[n][r] == 0:
    #             self.comb[n][r] = self.ncr(n, r)
    #         return self.comb[n][r]
    #     else:
    #         return self.ncr(n, r)

    # def combination_climbStairs(self, n: int) -> int:
    #     inc, result = 1, 0
    #     while(n > 2*inc):
    #         result += self.get_ncr(n-inc, inc)
    #         inc += 1

    #     if n%2 == 1:
    #         result += 1
    #     else:
    #         result += 2
    #     return int(result)

    def __init__(self):
        self.dynamic_table = numpy.zeros(shape=(1000,), dtype=int)
        
        self.dynamic_table[1] = 1
        self.dynamic_table[2] = 2

    def climbStairs(self, n: int) -> int:
        if len(self.dynamic_table) > n:
            if self.dynamic_table[n] == 0 :
                self.dynamic_table[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
            return int(self.dynamic_table[n])
        else:
            return int(self.climbStairs(n-1)) + int(self.climbStairs(n-2))

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            n = int(line);
            
            ret = Solution().climbStairs(n)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()