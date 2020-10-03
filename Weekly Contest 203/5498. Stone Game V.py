from typing import List
class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        cost = 0
        # https://stackoverflow.com/a/890500
        def team(t):
            iterations = range(2, (len(t)//2) + 1)

            totalscore = sum(t)
            halftotalscore = totalscore/2.0

            oldmoves = {}
            for p in t:
                people_left = t[:]
                people_left.remove(p)
                oldmoves[p] = people_left

            if len(iterations) > 0:
                for _ in iterations:
                    newmoves = {}
                    for total, roster in oldmoves.items():
                        for p in roster:
                            people_left = roster[:]
                            people_left.remove(p)
                            newtotal = total+p
                            if newtotal > halftotalscore: 
                                continue
                            newmoves[newtotal] = people_left
                    oldmoves = newmoves
            solution = min(map(lambda i: (abs(float(i)-halftotalscore), i), oldmoves.keys()))
            # return (solution[1], sum(oldmoves[solution[1]]), oldmoves[solution[1]])
            if solution[1] > sum(oldmoves[solution[1]]):
                return sum(oldmoves[solution[1]]), oldmoves[solution[1]]
            else:
                for a in oldmoves[solution[1]]:
                    t.remove(a)
                return solution[1], t
        while len(stoneValue) > 0:
            temp, stoneValue = team(stoneValue)
            print(temp, stoneValue)
            cost += temp
        return cost

obj = Solution()
# print(18, obj.stoneGameV( stoneValue = [6,2,3,4,5,5]))
# print(28, obj.stoneGameV( stoneValue = [7,7,7,7,7,7,7]))
# print(0,  obj.stoneGameV( stoneValue = [4]))