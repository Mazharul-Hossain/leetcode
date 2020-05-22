class Solution:

    def cmp(self, a, b):
        return (a > b) - (a < b) 

    def stoneGameIII(self, stoneValue: [int]) -> str:
        # ################
        # fails for greedy
        # print( "Tie", obj.stoneGameIII( stoneValue = [-1,-2,-3]) ) 
        # 
        # sum_A, sum_B = 0, 0
        # move_selector, pointer = True, 0

        # length = len( stoneValue )
        # while pointer < length :
        #     move_pointer, max_pointer = 1, 0
        #     max_sum, sum = stoneValue[pointer], stoneValue[pointer]
            
        #     while pointer + move_pointer < length and move_pointer < 3:
        #         sum += stoneValue[pointer + move_pointer]
        #         if sum > max_sum:
        #             max_sum = sum
        #             max_pointer = move_pointer
        #         move_pointer += 1
                
        #     pointer = pointer + max_pointer + 1

        #     if move_selector:
        #         sum_A += max_sum
        #     else:
        #         sum_B += max_sum
        #     move_selector = not move_selector
        
        # if sum_A > sum_B:
        #     return "Alice"
        # elif sum_A < sum_B:
        #     return "Bob"
        # else:
        #     return "Tie"
        # ################
        
        # DP for now
        dp = [0] * 3
        for i in range( len(stoneValue) - 1, -1, -1):
            dp[i % 3] = max( sum( stoneValue[i : i + k] ) - dp[ (i + k) % 3 ] for k in (1, 2, 3) )
        return ["Tie", "Alice", "Bob"][self.cmp(dp[0], 0)]


obj = Solution()
print( "Bob", obj.stoneGameIII( stoneValue = [1,2,3,7] ) )
print( "Alice", obj.stoneGameIII( stoneValue = [1,2,3,-9] ) )
print( "Tie", obj.stoneGameIII( stoneValue = [1,2,3,6] ) )
print( "Alice", obj.stoneGameIII( stoneValue = [1,2,3,-1,-2,-3,7] ) )
print( "Tie", obj.stoneGameIII( stoneValue = [-1,-2,-3]) ) # fails for greedy
