class Solution:
    """
    cases:
        if already sorted ----> return True
        else :
            roated means check for changes and with that x value find sorted or not
    """
    def check(self, nums: List[int]) -> bool:
        sortedNums = sorted(nums)

        if( nums == sortedNums):
            return True

        n = len(nums)
        pos = 0
        for i in range(n-1):
            if( nums[i] > nums[i+1]):
                break
            else:
                pos += 1
        
        for i in range(n):
            
            if( nums[(i + pos+1) % n] != sortedNums[i]):
                return False
        return True
        