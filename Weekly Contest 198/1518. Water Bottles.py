class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        max_drink = numBottles
        while (numBottles // numExchange) > 0:
            max_drink += numBottles // numExchange
            numBottles = (numBottles // numExchange) + (numBottles % numExchange)

        return max_drink