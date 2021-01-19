from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # https://stackoverflow.com/a/2173873
        boxTypes.sort(key=lambda x: x[1], reverse=True)

        maximum_total_units, index = 0, 0
        while truckSize > 0 and index < len(boxTypes):
            numberOfBoxes, numberOfUnitsPerBox = boxTypes[index]
            if numberOfBoxes < truckSize:
                maximum_total_units += numberOfBoxes * numberOfUnitsPerBox
            else:
                maximum_total_units += truckSize * numberOfUnitsPerBox
            truckSize -= numberOfBoxes
            index += 1
        return maximum_total_units


obj = Solution()
print(obj.maximumUnits(boxTypes=[[1, 3], [2, 2], [3, 1]], truckSize=4))
print(obj.maximumUnits(boxTypes=[[5, 10], [2, 5], [4, 7], [3, 9]], truckSize=10))
