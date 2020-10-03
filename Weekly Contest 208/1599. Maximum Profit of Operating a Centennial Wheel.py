from typing import List


class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if boardingCost * 4 < runningCost:
            return -1
        customer_counter, gain, max_gain, min_index, i = 0, 0, 0, -1, 0
        while i < len(customers) or customer_counter > 0:
            if i < len(customers):
                customer_counter += customers[i]
            i += 1

            if customer_counter >= 4:
                customer = 4
                customer_counter -= 4
            else:
                customer = customer_counter
                customer_counter = 0

            gain += customer * boardingCost - runningCost
            # print(i, customer_counter, gain)
            if gain > 0 and max_gain < gain:
                max_gain = gain
                min_index = i
        return min_index


obj = Solution()
# print(3, obj.minOperationsMaxProfit(customers=[8, 3], boardingCost=5, runningCost=6))
# print(7, obj.minOperationsMaxProfit(customers=[10, 9, 6], boardingCost=6, runningCost=4))
# print(-1, obj.minOperationsMaxProfit(customers=[3, 4, 0, 5, 1], boardingCost=1, runningCost=92))
# print(9, obj.minOperationsMaxProfit(customers=[10, 10, 6, 4, 7], boardingCost=3, runningCost=8))
# print(-1, obj.minOperationsMaxProfit(customers=[3, 4, 0, 5, 1], boardingCost=1, runningCost=4))
print(-1, obj.minOperationsMaxProfit(customers=[3, 4, 25, 5, 1], boardingCost=1, runningCost=4))
