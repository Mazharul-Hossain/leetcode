from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}

        for word in strs:
            key = ''.join(sorted(word))
            if key not in dict:
                dict[key] = [] 
            dict[key].append(word)
        
        list_result = []
        for key, value in dict.items():
            list_result.append(value)
        return list_result


obj = Solution()
print( obj.groupAnagrams( strs = ["eat", "tea", "tan", "ate", "nat", "bat"] ) )