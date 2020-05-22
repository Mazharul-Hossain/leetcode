from typing import List
import numpy

class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        # brute force
        # https://stackoverflow.com/a/16579295/2049763
        flag_list, len_list = [], []

        for i in range( len(favoriteCompanies)):
            len_list.append( len(favoriteCompanies[i]) )
            flag_list.append(True) 
            favoriteCompanies[i] = set(favoriteCompanies[i])

        sorted_len_list = numpy.argsort(len_list)[::-1]
        
        for i_1 in range( len( sorted_len_list)):
            i = sorted_len_list[i_1]
            for j_1 in range(i_1+1, len(sorted_len_list)):
                j = sorted_len_list[j_1]
                if flag_list[j] and favoriteCompanies[j].issubset(favoriteCompanies[i]):
                    flag_list[j] = False
        
        return_list = []
        for i in range( len( flag_list)):
            if flag_list[i] :
                return_list.append(i)
        return return_list

obj = Solution()
print( [0,1,4], obj.peopleIndexes( favoriteCompanies = [["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]] ) )
print( [0,1], obj.peopleIndexes( favoriteCompanies = [["leetcode","google","facebook"],["leetcode","amazon"],["facebook","google"]] ) )
print( [0,1,2,3], obj.peopleIndexes( favoriteCompanies = [["leetcode"],["google"],["facebook"],["amazon"]] ) )