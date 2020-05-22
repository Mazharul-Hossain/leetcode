from itertools import combinations
class Solution:
    def numTeams(self, rating: [int]) -> int:
        my_combinations = combinations(rating, 3)

        count = 0
        for combination in my_combinations:
            l_ref = list(combination)

            l_min = list(combination)
            l_min.sort()

            # print("l_min", l_ref, l_min)
            if l_ref == l_min:
                count += 1
                continue
            
            l_max = list(combination)
            l_max.sort()
            l_max.reverse()
            
            # print("l_max", l_ref, l_max)
            if l_ref == l_max:
                count += 1
        return count


obj = Solution()
print( 3, obj.numTeams( rating = [2,5,3,4,1] ) )       
print( 0, obj.numTeams( rating = [2,1,3] ) )
print( 2, obj.numTeams( rating = [2,1,3,4] ) )
print( 4, obj.numTeams( rating = [1,2,3,4] ) )