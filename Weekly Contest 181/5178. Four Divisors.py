import math
MAX_NUM = 100001
# MAX_NUM = 100

class Solution:
    # def __init__(self):
    #     self.prime = []
    #     self.find_prime()

    #     self.four_divisor = []
    #     # self.find_n_divisor()

    # def find_prime(self):
    #     is_prime = [True] * MAX_NUM
    #     smallest_prime_factor = [None] * MAX_NUM

    #     is_prime[0] = is_prime[1] = False
    #     # https://www.geeksforgeeks.org/sieve-eratosthenes-0n-time-complexity/
    #     for i in range(2, MAX_NUM):
    #         if is_prime[i]:
    #             self.prime.append(i)
    #             smallest_prime_factor[i] = i

    #         j = 0
    #         while (j < len(self.prime) and
    #                 i * self.prime[j] < MAX_NUM and
    #                 self.prime[j] <= smallest_prime_factor[i]): 
            
    #             is_prime[ i * self.prime[j] ] = False
    
    #             # put smallest prime factor of i*prime[j]  
    #             smallest_prime_factor[ i * self.prime[j] ] = self.prime[j] 
                
    #             j += 1
    #     # print(self.prime)

    # def find_n_divisor(self, n=4):
    #     self.four_divisor = [False] * MAX_NUM
    #     # Traversing all numbers in given range  
    #     for i in range(4, MAX_NUM):
    #         # initializing temp as i  
    #         temp = i
    #         # total holds the number of divisors of i  
    #         total = 1
    #         loop_limit = math.sqrt(i)
    #         for prime in self.prime:
    #             if prime > loop_limit:
    #                 break 
                
    #             # holds the exponent of k in prime factorization of i  
    #             count = 0  
    
    #             # repeatedly divide temp by k till it is  
    #             # divisible and accordingly increase count  
    #             while (temp % prime == 0): 
    #                 count += 1
    #                 temp = temp // prime
    
    #             # using the formula no.of divisors =  
    #             # (e1+1)*(e2+1)....  
    #             total = total * (count + 1)
    
    #         # if temp is not equal to 1 then there is  
    #         # prime number in prime factorization of i  
    #         # greater than sqrt(i)  
    #         if (temp != 1):  
    #             total = total * 2
    #         if total == 4:
    #             self.four_divisor[i] = True

    # def sumFourDivisors(self, nums: [int]) -> int:        
    #     prime_set = set(self.prime)

    #     sum = 0
    #     for num in nums:
    #         if num == 8:
    #             sum += 15
    #             continue
    #         loop_limit = math.sqrt(num)
    #         for prime in self.prime:
    #             # print(prime)
    #             if prime > loop_limit:
    #                 break
    #             if (num % prime) == 0:
    #                 divisor = num // prime
    #                 if divisor == prime:
    #                     continue
    #                 if divisor in prime_set:
    #                     # print(prime, divisor)
    #                     # print(1, num, prime, divisor)
    #                     sum = sum + 1 + num + prime + divisor
    #     return sum

    def sumFourDivisors(self, nums: [int]) -> int:
        ans = 0
        for num in nums:
            ans += self.fourDivisors(num)
        return ans

    # dumb style works fine    
    def dumb_fourDivisors(self, num):
        memo = set()
        for i in range(1, num + 1):
            if i * i > num:
                break
            if num % i == 0:
                memo.add(i)
                memo.add(num // i)
        if len(memo) == 4:
            return sum(memo)
        return 0
        
    def fourDivisors(self, num):
        memo = set()
        loop_limit = math.sqrt(num)
        for i in range(1, loop_limit + 1):
            if num % i == 0:
                memo.add(i)
                memo.add(num // i)
        if len(memo) == 4:
            return sum(memo)
        return 0


obj = Solution()
print( 32, obj.sumFourDivisors( nums = [21,4,7] ) )
print( 45, obj.sumFourDivisors( nums = [1,2,3,4,5,6,7,8,9,10] ) )