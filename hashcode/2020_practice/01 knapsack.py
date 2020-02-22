import numpy

class Solution:
    def get_pizza_list(self, value_list: [int], knapsack_list: [[int]]):
        item, capacity = len(knapsack_list) - 1, len(knapsack_list[0]) - 1
        pizza_list = []
        while(knapsack_list[item][capacity] > 0):
            if knapsack_list[item][capacity] > knapsack_list[item - 1][capacity]:
                pizza_list.append(item - 1)
                item -= 1
                capacity -= value_list[item]
            else:
                item -= 1
        pizza_list.reverse()
        return pizza_list

    def knapsack(self, value_list: [int], capacity: int) -> None:
        knapsack_list = [[0 for j in range(capacity + 1)] for i in range(len(value_list) + 1)]

        for i in range(1, len(value_list) + 1):
            for j in range(1, capacity+1):
                if value_list[i - 1] > j:
                    knapsack_list[i][j] = knapsack_list[i - 1][j]
                else:
                    knapsack_list[i][j] = max(
                        value_list[i - 1] + knapsack_list[i-1][j - value_list[i - 1]], 
                        knapsack_list[i - 1][j - 1] )
        return knapsack_list

    def read_input_pizza(self, filename):
        lines = open(filename).readlines()
        M, N = [int(val) for val in lines[0].split()]
        pizza = numpy.array([int(val) for val in lines[1].split()])
        return M, N, pizza

# knapsack_list = Solution().knapsack([2,4,6,8], 10)
# print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in knapsack_list]))
obj = Solution()
M, N, pizza = obj.read_input_pizza("d_quite_big.in")
print(M, N, pizza)

knapsack_list = obj.knapsack(pizza, M)
print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in knapsack_list]))

pizza_list = obj.get_pizza_list(pizza, knapsack_list)
print("pizza list:\t", '\t'.join([str(cell) for cell in pizza_list]))
