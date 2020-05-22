class Solution:
    def findLucky(self, arr: [int]) -> int:
        arr.reverse()

        hash_map = {}
        for a in arr: 
            if a not in hash_map:
                hash_map[a] = 0
            hash_map[a] += 1
        
        arr = list( set( arr ) )
        arr.reverse()

        for a in arr:
            if a == hash_map[a]:
                return a
        return -1
             
            
obj = Solution()
print( obj.findLucky(arr = [2,2,3,4]) )
print( obj.findLucky( arr = [1,2,2,3,3,3] ) )
print( obj.findLucky( arr = [2,2,2,3,3] ) )
print( obj.findLucky( arr = [5] ) )
print( obj.findLucky( arr = [7,7,7,7,7,7,7] ) )

print( obj.findLucky( arr = [5,4,7,8,4,8,8,3,7,7,6,3,7,6,5,6,8,4,5,7,4,7,7,5,2,5,6,6,8,1,6,8,8,8,9,3,2,9] ) )