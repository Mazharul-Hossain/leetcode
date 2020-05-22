class Solution:
    def arrangeWords(self, text: str) -> str:
        text = text.lower().split()

        dict = {}
        for word in text:
            key = len(word)
            if key not in dict:
                dict[key] = ""
            dict[key] += word + " "
        keys = list(dict.keys())
        keys.sort()

        return_string = ""
        for key in keys:
            return_string += dict[key]
        return return_string.rstrip().capitalize() 
         

obj = Solution()
print( "Is cool leetcode # ", obj.arrangeWords( text = "Leetcode is cool" ) )
print( "On and keep calm code # ", obj.arrangeWords( text = "Keep calm and code on" ) )
print( "To be or to be not # ", obj.arrangeWords( text = "To be or not to be" ) )