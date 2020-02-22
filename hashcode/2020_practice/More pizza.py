# https://flothesof.github.io/preparing-hashcode-2018.html

import numpy
import os

class Solution:
    def get_pizza_list(self, value_list: [int], knapsack_list: [[int]]):
        item, capacity = len(knapsack_list) - 1, len(knapsack_list[0]) - 1
        pizza_list, total_value = [], knapsack_list[item][capacity]

        while(knapsack_list[item][capacity] > 0):
            if knapsack_list[item][capacity] > knapsack_list[item - 1][capacity]:
                pizza_list.append(item - 1)
                item -= 1
                capacity -= value_list[item]
            else:
                item -= 1
        pizza_list.reverse()
        return total_value, len(pizza_list), pizza_list

    def dp_knapsack(self, value_list: [int], capacity: int) -> [[int]]:
        knapsack_list = [[0 for j in range(capacity + 1)]]

        for i in range(1, len(value_list) + 1):
            row = [0]
            for j in range(1, capacity+1):
                if value_list[i - 1] > j:
                    row.append(knapsack_list[i - 1][j])
                else:
                    row.append( max(
                        value_list[i - 1] + knapsack_list[i-1][j - value_list[i - 1]], 
                        knapsack_list[i - 1][j] ) )
            knapsack_list.append(row)
        return knapsack_list

    def write_output_pizza(self, filename, pizza_list, suffix = None):        
        base = os.path.splitext(os.path.basename(filename))[0]
        if suffix is not None:
            base = base + "_" + suffix

        f = open(base + ".out", "w")
        f.write(str(len(pizza_list)) + "\r")
        f.write('\t'.join([str(cell) for cell in pizza_list]))

    
    def read_input_pizza(self, filename):
        lines = open(filename).readlines()
        M, N = [int(val) for val in lines[0].split()]
        pizza = numpy.array([int(val) for val in lines[1].split()])
        return M, N, pizza

    def greedy_knapsack(self, value_list: [int], capacity: int):
        pizza_list, total_value = [], 0
        for i in range(len(value_list) - 1, -1, -1):
            if capacity <= 0:
                break
            if value_list[i] <= capacity:
                pizza_list.append(i)
                total_value += value_list[i] 
                capacity -= value_list[i]
        pizza_list.reverse()
        return total_value, len(pizza_list), pizza_list

    def solve_greedy(self, file_name, M, N, pizza):
        total_value, number_pizza, pizza_list = self.greedy_knapsack(pizza, M)
        print(total_value, number_pizza, "\ngreedy pizza list:\t", '\t'.join([str(cell) for cell in pizza_list]))
        self.write_output_pizza(file_name, pizza_list, "greedy")

    def solve_dp(self, file_name, M, N, pizza):
        knapsack_list = self.dp_knapsack(pizza, M)
        # print('\n\n'.join(['\t'.join([str(cell) for cell in row]) for row in knapsack_list]))

        total_value, number_pizza, pizza_list = self.get_pizza_list(pizza, knapsack_list)
        print(total_value, number_pizza, "\ndp pizza list:\t", '\t'.join([str(cell) for cell in pizza_list]))
        self.write_output_pizza(file_name, pizza_list, "dp")



obj = Solution()
for file_name in ["a_example.in", "b_small.in", "c_medium.in", "d_quite_big.in", "e_also_big.in"]: 
    print("\n#=====Running for: ", file_name, "=====#")

    M, N, pizza = obj.read_input_pizza(file_name)
    # print(M, N, pizza)
    
    if M * N <= 100000000:
        obj.solve_dp(file_name, M, N, pizza)
    else:
        obj.solve_greedy(file_name, M, N, pizza)

    