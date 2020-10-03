class Solution:
    def minFlips(self, target: str) -> int:
        counter, same, flag = 0, "", True
        for b in target:
            if flag and b == "0":
                continue
            elif flag and b == "1":
                flag = False
                same = b
                counter += 1
            else:
                if b == same:
                    continue
                else:
                    same = b
                    counter += 1
        return counter

obj = Solution()
print(obj.minFlips( target = "00000" ))
print(obj.minFlips( target = "10111" ))
print(obj.minFlips( target = "0010000111010" ))
print(obj.minFlips( target = "1" ))
print(obj.minFlips( target = "01" ))
print(obj.minFlips( target = "10" ))