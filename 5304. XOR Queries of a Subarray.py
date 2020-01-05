class Solution:
    def xorQueries(self, arr: [int], queries: [[int]]) -> [int]:
        # A simple solution
        # output_list = []
        # for query_range in queries:
        #     output = arr[query_range[0]]
        #     for index in range(query_range[0] + 1, query_range[1] + 1):
        #         output ^= arr[index]
        #     output_list.append(output)
        # return output_list
        ####################
        xor_calculator = [
            [0 for j in range(32)]
               for i in range(len(arr))
        ]
        for j in range(32):
            for i in range(len(arr)):
                if i > 0:
                    xor_calculator[i][j] = xor_calculator[i-1][j]
                # print(arr[i], (1 << j) ,(arr[i] & (1 << j)))
                if (arr[i] & (1 << j)):                    
                    xor_calculator[i][j] += 1
                    # print("xor_calculator:", i, j, xor_calculator[i][j])
        # print(xor_calculator)
        output_list = []
        for query_range in queries:
            output = 0
            if query_range[1] == query_range[0]:
                output = arr[query_range[1]]
            else:
                # print("range:", query_range[0], query_range[1])
                for index in range(32):
                    if query_range[0] == 0:
                        counter = xor_calculator[query_range[1]][index]
                    else:
                        counter = xor_calculator[query_range[1]][index] - xor_calculator[query_range[0]-1][index]                    
                    if (counter & 1):
                        output += (1 << index)
                        # print(index, counter, (2 << (index-1)))
            output_list.append(output)
        return output_list


arr = [1,3,4,8]
queries = [[0,1],[1,2],[0,3],[3,3]]
print([2,7,14,8], Solution().xorQueries(arr, queries))

arr = [4,8,2,10]
queries = [[2,3],[1,3],[0,0],[0,3]]
print([8,0,4,4], Solution().xorQueries(arr, queries))