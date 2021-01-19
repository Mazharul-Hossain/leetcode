# The knows API is already defined for you.
# return a bool, whether a knows b
def knows(a: int, b: int) -> bool:
    pass


class Solution:
    def findCelebrity(self, n: int) -> int:
        counter, not_celebrity = 0, set()

        for a in range(n):
            for b in range(n):
                if a == b or b in not_celebrity:
                    continue
                flag = knows(a, b)  # if b is celebrity
                counter += 1

                if not flag:
                    not_celebrity.add(b)
                else:
                    not_celebrity.add(a)

        for a in range(n):
            if a not in not_celebrity:
                for b in range(n):
                    if a == b:
                        continue
                    flag = knows(a, b)  # if a knows some one
                    counter += 1

                    if flag:
                        not_celebrity.add(a)
                        break
            if a not in not_celebrity:
                return a
        print(counter)
        return -1
