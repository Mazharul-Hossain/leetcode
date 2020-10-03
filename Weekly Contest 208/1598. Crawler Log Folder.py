from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0
        for log in logs:
            if log == "../":
                if depth > 0:
                    depth -= 1
            elif log == "./":
                pass
            else:
                depth += 1
        return depth


obj = Solution()
print(2, obj.minOperations(logs=["d1/", "d2/", "../", "d21/", "./"]))
print(3, obj.minOperations(logs=["d1/", "d2/", "./", "d3/", "../", "d31/"]))
print(0, obj.minOperations(logs=["d1/", "../", "../", "../"]))
print(0, obj.minOperations(logs=["./", "../", "./"]))
