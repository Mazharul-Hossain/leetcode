class Solution:
    def reformat(self, s: str) -> str:

        alphabet, digit = [], []
        for ch in s:        
            if((ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z')): 
                alphabet.append(ch) 
            elif(ch >= '0' and ch <= '9'):
                digit.append(ch)

        if len(alphabet) == len(digit) or len(alphabet) + 1 == len(digit):
            one = digit
            two = alphabet
        elif len(alphabet) - 1 == len(digit):
            one = alphabet
            two = digit            
        else:
            return ""
        if len(one) == 0: 
            return "" 
        if len(one) == 1 and len(two) == 0: 
            return "".join(one)

        return_string, i = [], 0
        for i in range(len(two)):
            return_string.append( one[i] )
            return_string.append( two[i] )
        
        if i + 1 < len(one):  
            return_string.append( one[i + 1] )

        return "".join(return_string)


obj = Solution()

print( "0a1b2c", obj.reformat( s = "a0b1c2" ) )
print( "", obj.reformat( s = "leetcode" ) )
print( "", obj.reformat( s = "1229857369" ) )
print( "", obj.reformat( s = "1229857369" ) )
print( "c2o0v1i9d", obj.reformat( s = "covid2019" ) )
print( "1a2b3", obj.reformat( s = "ab123" ) )
print( "a", obj.reformat( s = "a" ) )