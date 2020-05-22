class Solution:
    def findDuplicate(self, s: str) -> bool:
        list_s = list(s)
        set_s = set(list_s)

        if len(list_s) == len(set_s):
            return False
        return True

    def lengthOfLongestSubstring(self, s: str) -> int:
        # Difference between SubArray, SubSequence and SubSet
        # https://youtu.be/qoI26oy8MeI
        head, tail, max_return = 0, 0, 0
        hash_set = set()
        while tail < len(s) and head < len(s):
            if s[tail] not in hash_set:
                hash_set.add(s[tail])
                tail += 1

                max_return = max(max_return, len(hash_set))
            else:
                while head < tail: 
                    hash_set.remove( s[head] )
                    head += 1

                    if s[head-1] == s[tail]:
                        break
        return max_return



obj = Solution()
print(3, obj.lengthOfLongestSubstring( s = "abcabcbb" ) )
print(1, obj.lengthOfLongestSubstring( s = "bbbbb" ) )
print(3, obj.lengthOfLongestSubstring( s = "pwwkew" ) )