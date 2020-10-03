#!/bin/python3

import math
import os
import random
import re
import sys
from typing import List

# Class to represent a job 
class Jewel: 
    def __init__(self, start, end, profit): 
        self.start  = start 
        self.end = end 
        self.profit  = profit 

def expandAroundCenter(s, left, right) -> Jewel:
    counter = 0
    while left >= 0 and right < len(s) and s[left] == s[right]:
        counter += 1

        left -= 1
        right += 1
    return Jewel(left+1, right-1, counter)

def longestPalindrome(s: str) -> List[Jewel]:
    jewels = []
    for i in range( len(s) - 1):
        jewel = expandAroundCenter(s, i, i+1)
        if jewel.profit > 0:
            jewels.append(jewel)
    return jewels

# A Binary Search based function to find the latest job 
# (before current job) that doesn't conflict with current 
# job.  "index" is index of the current job.  This function 
# returns -1 if all jobs before index conflict with it. 
# The array jobs[] is sorted in increasing order of finish 
# time. 
def binarySearch(jewels:List[Jewel], start_index: int) -> int: 
  
    # Initialize 'lo' and 'hi' for Binary Search 
    lo = 0
    hi = start_index - 1
  
    # Perform binary Search iteratively 
    while lo <= hi: 
        mid = (lo + hi) // 2
        if jewels[mid].end <= jewels[start_index].start: 
            if jewels[mid + 1].end <= jewels[start_index].start: 
                lo = mid + 1
            else: 
                return mid 
        else: 
            hi = mid - 1
    return -1

#
# Complete the 'getMaxScore' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING jewels as parameter.
#

# https://www.geeksforgeeks.org/weighted-job-scheduling-log-n-time/
def getMaxScore(jewels: str):
    if jewels is None or len(jewels) == 0:
        return 0
    # Write your code here
    jewels = longestPalindrome(jewels)
    # Sort jobs according to finish time 
    jewels = sorted(jewels, key = lambda j: j.end) 
  
    # Create an array to store solutions of subproblems.  table[i] 
    # stores the profit for jobs till arr[i] (including arr[i]) 
    n = len(jewels)
    if n == 0:
        return 0  
    table = [0 for _ in range(n)] 
  
    table[0] = jewels[0].profit
  
    # Fill entries in table[] using recursive property 
    for i in range(1, n): 
  
        # Find profit including the current job 
        inclProf = jewels[i].profit 
        l = binarySearch(jewels, i) 
        if (l != -1):
            inclProf += table[l]
  
        # Store maximum of including and excluding 
        table[i] = max(inclProf, table[i - 1]) 
  
    return table[n-1]

print(getMaxScore("abcddcbaabcddcbd"))
print(getMaxScore("abcddcba"))
print(getMaxScore("aabbccddee"))
print(getMaxScore(""))
