class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split()
        length = len(searchWord)
        for key, word in enumerate(words):
            if len(word) < length:
                continue
            if word.startswith(searchWord):
                return key + 1
        return -1



obj = Solution()
print( 4, obj.isPrefixOfWord( sentence = "i love eating burger", searchWord = "burg" ) )
print( 2, obj.isPrefixOfWord( sentence = "this problem is an easy problem", searchWord = "pro" ) )
print( -1, obj.isPrefixOfWord( sentence = "i am tired", searchWord = "you" ) )
print( 4, obj.isPrefixOfWord( sentence = "i use triple pillow", searchWord = "pill" ) )
print( -1, obj.isPrefixOfWord( sentence = "hello from the other side", searchWord = "they" ) )