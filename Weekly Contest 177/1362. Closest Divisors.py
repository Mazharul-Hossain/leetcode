class Solution:
    def closestDivisors(self, num: int) -> [int]:
        num1, num2 = num + 1, num + 2

        import math
        divisor1, divisor2 = num1, num2
        if num > 1:
            divisor1, divisor2 = int(math.sqrt(num1)), int(math.sqrt(num2))

        while(divisor1 > 1 or divisor2 > 1):
            diff1, diff2 = -1, -1
            
            if divisor1 > 1:
                if num1 % divisor1 == 0:
                    divident1 = num1 // divisor1
                    diff1 = abs(divisor1 - divident1)  
            
            if divisor2 > 1:
                if num2 % divisor2 == 0:
                    divident2 = num2 // divisor2
                    diff2 = abs(divisor2 - divident2)

            if diff1 > -1 and diff2 > -1:
                if diff1 > diff2:
                    return [divisor2, divident2]
                else: 
                    return [divisor1, divident1]
            
            elif diff1 > -1:
                return [divisor1, divident1]
            
            elif diff2 > -1:
                return [divisor2, divident2]

            divisor1 -= 1
            divisor2 -= 1


obj = Solution()

print(obj.closestDivisors(1))
print(obj.closestDivisors(2))
print(obj.closestDivisors(3))
print(obj.closestDivisors(8))
print(obj.closestDivisors(123))
print(obj.closestDivisors(999))