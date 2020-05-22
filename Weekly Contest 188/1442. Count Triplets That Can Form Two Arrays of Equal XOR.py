from typing import List

class Solution:
    # Function to preprocess the array and  
    # find count of number of ones up to jth index for ith bit. 
    def preprocess(arr, n):
        count = []
    
        # Run a loop for each bit position from 0 to 32. 
        for i in range(32): 
            temp_count = [0]
            for j in range(n): 
                if (j > 0):     
                    # store previous count  of 1s  for ith bit position. 
                    temp_count.append( temp_count[j - 1] )  
    
                # Check if ith bit for jth element of array is set or not. 
                # If it is set then increase count  of 1 for ith bit by 1. 
                if (arr[j] & (1 << i)): 
                    temp_count[j] += 1
            count.append(temp_count)
            print(i," : ", count)
        return count
    
    # Function to find XOR value for a range of array elements. 
    def findXOR(L, R, count): 
    
        # variable to store final answer. 
        ans = 0
    
        # variable to store number of 1s for ith bit in the range L to R. 
        noOfOnes = 0
    
        # Find number of 1s for each bit position from 0 to 32. 
        for i in range(32): 
            if L > 0: 
                noOfOnes = count[i][R] - count[i][L - 1] 
            else: 
                noOfOnes = count[i][R] 
    
            # If number of 1s are odd then in the result 
            # ith bit will be set, i.e., 2^i will be  
            # present in the result. Add 2^i in ans variable. 
            if (noOfOnes & 1): 
                ans += (1 << i) 
    
        return ans

    # https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/discuss/623747/JavaC%2B%2BPython-One-Pass-O(N4)-to-O(N)
    def countTriplets(self, arr: List[int]) -> int:
        # Solution 5: Prefix XOR, One Pass
        result = current = 0
        count = {0: [1, -1]}
        for k, a in enumerate(arr):
            current ^= a
            if current not in count:
                count[current] = [0, 0]
            n, total = count[current]
            result += (k - 1) * n - total
            count[current] = [n + 1, total + k]
        return result
        
        