from collections import deque


class Solution:
    # https://leetcode.com/problems/check-if-string-is-transformable-with-substring-sort-operations/discuss/843917/C++JavaPython-O(n)/694626
    def isTransformable(self, s: str, t: str) -> bool:
        idx = [deque() for _ in range(10)]

        for i, ch in enumerate(s):
            idx[int(ch)].append(i)

        for ch in t:
            print(idx)
            d = int(ch)

            if not idx[d]:
                print("1# dead cause")
                return False

            for i in range(d):
                if idx[i]:
                    print("1# running: position of {} is {} and position of {} is {}".format(
                        i, idx[i][0], d, idx[d][0]))

                    if idx[i][0] < idx[d][0]:
                        print("2# dead cause: position of {} is {} and position of {} is {}".format(
                            i, idx[i][0], d, idx[d][0]))
                        return False
            idx[d].popleft()
        return True


obj = Solution()
print(obj.isTransformable(s="84532", t="34852"))
print(obj.isTransformable(s="34521", t="23415"))
print(obj.isTransformable(s="12345", t="12435"))
print(obj.isTransformable(s="1", t="2"))
