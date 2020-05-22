class Solution:
    # TL error not solved
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        croak = [ "c", "r", "o", "a", "k"]

        counter, flag_counter = 0, 0
        while True:
            pointer = 4
            for i in range( len(croakOfFrogs) - 1, -1, -1 ):
                if croak[pointer] == croakOfFrogs[i]:
                    pointer -= 1
                    croakOfFrogs = croakOfFrogs[0 : i] + croakOfFrogs[i + 1 : ]

                if pointer == -1:
                    pointer = 4
                    if counter == flag_counter:
                        counter += 1

            if counter == flag_counter:
                break
            flag_counter = counter
        if len(croakOfFrogs) != 0:
            return -1
        return counter

obj = Solution()

print( 1, obj.minNumberOfFrogs( croakOfFrogs = "croakcroak" ) )
print( 2, obj.minNumberOfFrogs( croakOfFrogs = "crcoakroak" ) )
print( -1, obj.minNumberOfFrogs( croakOfFrogs = "croakcrook" ) )
print( -1, obj.minNumberOfFrogs( croakOfFrogs = "croakcroa" ) )