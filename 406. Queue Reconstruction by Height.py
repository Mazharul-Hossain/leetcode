class Solution:
    def reconstructQueue(self, people: [[int]]) -> [[int]]:
        # https://leetcode.com/problems/queue-reconstruction-by-height/discuss/89359/Explanation-of-the-neat-Sort%2BInsert-solution
        height_list = sorted( ( -x[0], x[1] ) for x in people)

        new_people_list = []
        for p in height_list:
            new_people_list.insert( p[1], [ -p[0], p[1] ] )

        return new_people_list

obj = Solution()
print( obj.reconstructQueue( [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]] ) )



