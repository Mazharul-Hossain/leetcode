import sys
from typing import List


class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        shortest_distance = sys.maxsize
        word1_list, word2_list = [], []

        for i, word in enumerate(words):
            if word1 == word:
                word1_list.append(i)
            elif word2 == word:
                word2_list.append(i)
        i, j = 0, 0
        while i < len(word1_list) and j < len(word2_list):
            temp_dist = abs(word1_list[i] - word2_list[j])
            if temp_dist < shortest_distance:
                shortest_distance = temp_dist
            if word1_list[i] <= word2_list[j]:
                i += 1
            else:
                j += 1
        return shortest_distance
