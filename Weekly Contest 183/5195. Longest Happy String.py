import numpy
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        repeat = [a, b, c]
        repeat_str = ["a", "b", "c"]

        return_str, repeating = "", ""
        while True:
            if len(set(repeat)) == 1:
                return_str = return_str + "abc" * repeat[0]
                break

            sort_info = numpy.argsort(repeat)

            return_str = return_str + repeat_str[ sort_info[2] ]
            repeat[ sort_info[2] ] -= 1

            if repeating == repeat_str[ sort_info[2] ]:
                if repeat[ sort_info[1] ] == 0:
                    break

                return_str = return_str + repeat_str[ sort_info[1] ]
                repeat[ sort_info[1] ] -= 1

                repeating = repeat_str[ sort_info[1] ]
            else:
                repeating = repeat_str[ sort_info[2] ]

        return return_str

obj = Solution()
print( "ccaccbcc",  obj.longestDiverseString( a = 1, b = 1, c = 7 ) )
print( "aabbc",  obj.longestDiverseString( a = 2, b = 2, c = 1 ) )
print( "aabaa",  obj.longestDiverseString( a = 7, b = 1, c = 0 ) )