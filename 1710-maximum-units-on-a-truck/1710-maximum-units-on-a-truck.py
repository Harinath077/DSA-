class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # sorted boxType by units in decending order

        boxTypes.sort(key = lambda x: x[1], reverse = True)
        totalUnits = 0
        for box, units in boxTypes:
            take = min(box, truckSize)
            totalUnits += take * units
            # reduce the TruckSize
            truckSize -= take

            if( truckSize == 0):
                return totalUnits
        return totalUnits