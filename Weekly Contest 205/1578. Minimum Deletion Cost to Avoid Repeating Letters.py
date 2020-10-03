from typing import List
class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        c, i, length = 0, 0, len(s)
        while i < length-1:
            if s[i] == s[i+1]:
                sum_cost, max_cost = cost[i], cost[i]
                while i < length-1 and s[i] == s[i+1]:
                    sum_cost += cost[i+1]
                    max_cost = max(max_cost, cost[i+1])

                    i += 1
                c += (sum_cost - max_cost)   
            i += 1
        return c

obj =Solution()
print(3, obj.minCost(s = "abaac", cost = [1,2,3,4,5]))
print(0, obj.minCost(s = "abc", cost = [1,2,3]))
print(2, obj.minCost(s = "aabaa", cost = [1,2,3,4,1]))