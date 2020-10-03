from functools import lru_cache

class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        # https://leetcode.com/problems/string-compression-ii/discuss/755970/Python-dynamic-programming
        @lru_cache(None)
        # @lru_cache is the trick to do the memorization, otherwise, you have to handle the memorization yourself
        def counter(s: str, start: int, prev_char: str, count: int, remain_k: int): 
            # count increase from start            
            if remain_k < 0:
                return float('inf')
            if start >= len(s):
                return 0
            if s[start] == prev_char:                
                # keep it                
                incr = 1 if count == 1 or count == 9 or count == 99 else 0
                ans = incr + counter(s, start+1, prev_char, count+1, remain_k)
                print("#same_keep_it:", ans, start, prev_char, count, remain_k)
                return ans
            else:
				# keep it  
                ans1 = 1 + counter(s, start+1, s[start], 1, remain_k)                 
                print("#diff_keep_it:", ans1, start, prev_char, count, remain_k)                                        
                # delete it
                ans2 = counter(s, start + 1, prev_char, count, remain_k - 1)
                print("#diff_delete_it:", ans2, start, prev_char, count, remain_k)                

                return min(ans1, ans2)
            
        return counter(s, 0, "", 0, k)

obj = Solution()
print( 4, obj.getLengthOfOptimalCompression( s = "aaabcccd", k = 2 ))
print( 2, obj.getLengthOfOptimalCompression( s = "aabbaa", k = 2 ))
print("%%%%%%%%%%%%%%%%%%%%")
print( 3, obj.getLengthOfOptimalCompression( s = "aaaaaaaaaaa", k = 0 ))
print("%%%%%%%%%%%%%%%%%%%%")
print( 2, obj.getLengthOfOptimalCompression( s = "aaaaaaaaaaa", k = 2 ))