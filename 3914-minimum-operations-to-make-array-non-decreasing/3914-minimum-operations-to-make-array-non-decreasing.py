class Solution:
    
    """
    1. find the range
    2. find min in that range of Array 
    3. return ans = increasing - min
    """
    
    def minOperations(self, nums: list[int]) -> int:
            
        n = len(nums)

        if( n == 1 ):
            return 0
        
        # voilationg indices
        voilatingInd = []
        for i in range(n-1):
            # violation
            if( nums[i] > nums[i+1] ):
                voilatingInd.append(i+1)

        total = 0
        for index in voilatingInd:
            total += nums[index - 1] - nums[index]
        
        return total
                
     
        
            