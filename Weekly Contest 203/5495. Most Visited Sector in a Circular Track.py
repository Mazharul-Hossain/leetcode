from typing import List
class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        # counter = 0
        # for i in range(1, len(rounds)):
        #     if rounds[i] < rounds[i-1]:
        #         counter += n
        #     counter += (rounds[i] - rounds[i-1])
        #     counter = counter % n

        counter = (rounds[len(rounds)-1] - rounds[0] + n) % n
        start, ans = rounds[0], [rounds[0]]
        for i in range(1, counter+1):
            ans.append( n if (start+i)%n == 0 else (start+i)%n )
        return sorted(ans)

obj = Solution()
print(obj.mostVisited( n = 4, rounds = [1,3,1,2] ))
print(obj.mostVisited( n = 2, rounds = [2,1,2,1,2,1,2,1,2]))
print(obj.mostVisited( n = 7, rounds = [1,3,5,7]))
print(obj.mostVisited( n = 3, rounds = [3,2,1,2,1,3,2,1,2,1,3,2,3,1]))