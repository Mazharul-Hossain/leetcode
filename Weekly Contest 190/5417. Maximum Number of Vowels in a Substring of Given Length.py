class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        right, vowel_count, max_count = 0, 0, 0
        length = len(s)

        # s has no vowels not checked 
        while right < k and right < length:
            if s[right] in vowels:
                vowel_count += 1
            right += 1
        # if s is shorter than k is not checked
        max_count = vowel_count
        while right < length:
            if s[right-k] in vowels:
                vowel_count -= 1
            if s[right] in vowels:
                vowel_count += 1
            right += 1
            max_count = max(vowel_count, max_count)
        return max_count

obj = Solution()
print( 3, obj.maxVowels( s = "abciiidef", k = 3 ) )
print( 2, obj.maxVowels( s = "aeiou", k = 2 ) )
print( 2, obj.maxVowels( s = "leetcode", k = 3 ) )
print( 0, obj.maxVowels( s = "rhythms", k = 4 ) )
print( 1, obj.maxVowels( s = "tryhard", k = 4 ) )