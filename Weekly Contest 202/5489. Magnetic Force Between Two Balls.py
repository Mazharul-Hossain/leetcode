from typing import List
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        # https://www.geeksforgeeks.org/place-k-elements-such-that-minimum-distance-is-maximized/
        # https://stackoverflow.com/a/27971438
        def isFeasible(mid, position, n, m):       
            # Place first element at arr[0] position 
            # Initialize count of elements placed. 
            pos, elements = position[0], 1
        
            # Try placing k elements with minimum distance mid. 
            for i in range(1, n): 
                if position[i] - pos >= mid: 
                    print("old_pos:", pos, "new_pos:", position[i])
                    
                    # Place next element if its distance  
                    # from the previously placed element 
                    # is greater than current mid 
                    pos = position[i] 
                    elements += 1
        
                    # Return if all elements are placed successfully 
                    if (elements == m): 
                        return True
            return False

        position.sort()
        print(position)
        # Initialize result. 
        n = len(position)
    
        # Consider the maximum possible distance 
        left, right = 0, position[n - 1] - position[0] + 1
    
        # Do binary search for largest minimum distance 
        while right - left > 1: 
            mid = (left + right) // 2
            print(left, mid, right)
    
            # If it is possible to place k elements 
            # with minimum distance mid, search for 
            # higher distance. 
            if (isFeasible(mid, position, n, m)): 
                
                # Change value of variable max to mid iff 
                # all elements can be successfully placed 
                left = mid
    
            # If not possible to place k elements, search for lower distance 
            else: 
                right = mid  
        return left

obj = Solution()
# print(obj.maxDistance( position = [1,2,3,4,7], m = 3 ))
# print(obj.maxDistance( position = [5,4,3,2,1,1000000000], m = 2 ))
# print(obj.maxDistance( position = [79,74,57,22], m = 4 ))
print(3, obj.maxDistance( position = [1,2,3,4,5,6,7,8,9,10], m = 4 ))