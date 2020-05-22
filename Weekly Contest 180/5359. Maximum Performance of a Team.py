class Solution:
    def maxPerformance(self, n: int, speed: [int], efficiency: [int], k: int) -> int:
        modulo_factor = 10**9 + 7

        from queue import PriorityQueue
        performance_list = PriorityQueue()

        index = 0
        for s, e in zip( speed, efficiency ):
            performance_list.put( ( -s*e,  index) )
            index += 1

        speed_score, efficiency_score = 0, 0 
        while(performance_list.qsize() > 0 and k > 0):            
            _, index = performance_list.get()
            if speed_score == 0:
                speed_score, efficiency_score = speed[index], efficiency[index]
                k -= 1
            else:
                if efficiency_score <= efficiency[index]:
                    speed_score += speed[index]
                    k -= 1
                
        return ( (speed_score % modulo_factor) * efficiency_score) % modulo_factor



    
obj = Solution()
print( 60, obj.maxPerformance( n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2 ) )
print( 68, obj.maxPerformance( n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 3 ) )
print( 72, obj.maxPerformance( n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 4 ) )