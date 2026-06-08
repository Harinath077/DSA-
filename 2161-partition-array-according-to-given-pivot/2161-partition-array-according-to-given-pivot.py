class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        # brute force 

        if( len(nums) == 1):
            return nums
        
        less = []
        equal = []
        greater = []

        result = []
        for num in nums:
            if( num < pivot ):
                less.append(num)
            elif( num > pivot ):
                greater.append(num)
            else:
                equal.append(num)
        
        result.extend(less)
        result.extend(equal)
        result.extend(greater)
        
        return result
