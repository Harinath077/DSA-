class Solution:

    """
   note : there is many subarray range to modify
   s1 : find all volating indices and store
   s2 : with that find the each indices x value to added 
   s3 : cummulativily add that in toal variable and return 
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
                
     
        
            