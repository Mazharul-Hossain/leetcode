class Solution:
    def __init__(self):
        self.two_power = {}
        self.two_power[1] = 0
        self.two_power[2] = 1

    def convert_to_decimal(self, a):
        power = 1
        s = a[::-1]
        return_decimal = 0 
        for i in s:
            i = int(i)
            return_decimal += i * power
            power *= 2
        
        # print(a, s, return_decimal) 
        return return_decimal


    def numSteps(self, s: str) -> int:
        original = self.convert_to_decimal(s)
        
        save_stack, return_decimal = [], original 
        while return_decimal > 1:

            save_stack.append( return_decimal )

            if return_decimal in self.two_power:
                break
            
            if return_decimal % 2 == 0 :
                return_decimal = return_decimal // 2
            else: 
                return_decimal += 1 
        
        save_stack.reverse()
        for i in range(1, len( save_stack ) ) :
            self.two_power[ save_stack[i] ] = self.two_power[ save_stack[i -1] ] + 1

        return self.two_power[original]

obj = Solution()

print( 6,  obj.numSteps( s = "1101" ) )
print( 1,  obj.numSteps( s = "10" ) )
print( 0,  obj.numSteps( s = "1" ) )