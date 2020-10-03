#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'receivedText' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING S as parameter.
#

def receivedText(S):
    if S is None or len(S) == 0:
        return S
    result, temp, num_lock = [], [], False
    for c in S:
        # print(c, pointer)
        if c == "<":
            pointer = -1
        elif c == ">":
            pointer = len(result)-1
        elif c == "*":
            if pointer < 0 or pointer >= len(result):
                continue            
            del result[pointer]
        elif c == "#":
            num_lock = not num_lock
        else:
            if num_lock and c.isdigit():
                continue
            pointer += 1
            result.insert(pointer, c)
    result = temp + result
    return "".join(result)
            
            
        
    

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    S = input()

    result = receivedText(S)

    print(result)

    # fptr.write(result + '\n')

    # fptr.close()
