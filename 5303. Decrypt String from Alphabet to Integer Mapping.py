class Solution:
    def freqAlphabets(self, s: str) -> str:
        return_string = ""
        found_hash = False
        for i in range(len(s)-1, -1, -1):
            if s[i] == '#':
                found_hash = True
                multiplier = 1
                num = 0
            else:
                if found_hash:
                    num += int(s[i]) * multiplier
                    multiplier *= 10
                    if multiplier == 100:
                        return_string += str(chr(96 + num))
                        found_hash = False
                else:
                    return_string += str(chr(96 + int(s[i])))

        return return_string[::-1]

s = "10#11#12"
print("jkab", Solution().freqAlphabets(s))

s = "1326#"
print("acz", Solution().freqAlphabets(s))

s = "25#"
print("y", Solution().freqAlphabets(s))

s = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"
print("abcdefghijklmnopqrstuvwxyz", Solution().freqAlphabets(s))