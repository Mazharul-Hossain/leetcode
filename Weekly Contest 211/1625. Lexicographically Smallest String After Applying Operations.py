class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        queue, visited, ans = [s], set(), s

        counter = 0
        while len(queue) > 0:
            counter += 1

            temp = queue.pop(0)

            if temp in visited:
                continue
            visited.add(temp)
            ans = min(ans, temp)

            queue.append(self.add(temp, a))
            queue.append(self.rotate(temp, b))

        print(counter)
        return ans

    def add(self, s, a):
        temp, length = "", len(s)
        for i in range(length):
            if i % 2 == 0:
                temp += s[i]
            else:
                temp += chr(((ord(s[i]) - ord('0') + a) % 10) + ord('0'))
        return temp

    def rotate(self, temp, b):
        return temp[-b:] + temp[:-b]


obj = Solution()
print("2050" == obj.findLexSmallestString(s="5525", a=9, b=2))
print("24" == obj.findLexSmallestString(s="74", a=5, b=1))
print("0011" == obj.findLexSmallestString(s="0011", a=4, b=2))
print("00553311" == obj.findLexSmallestString(s="43987654", a=7, b=3))
