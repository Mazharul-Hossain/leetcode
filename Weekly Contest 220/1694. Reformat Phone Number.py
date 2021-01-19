import re


class Solution:
    def reformatNumber(self, number: str) -> str:
        number = re.split('[ \-]', number)
        number = "".join(number)
        count = len(number)

        i, answer = 0, ""
        while count > 4:
            answer += number[i:i + 3] + "-"
            count -= 3
            i += 3
        if count == 4:
            answer += number[i:i + 2] + "-" + number[i + 2:i + 4]
        else:
            answer += number[i:]
        return answer


obj = Solution()
print(obj.reformatNumber(number="1-23-45 6"))
print(obj.reformatNumber(number="123 4-567"))
print(obj.reformatNumber(number="123 4-5678"))
print(obj.reformatNumber(number="12"))
print(obj.reformatNumber(number="--17-5 229 35-39475 "))
