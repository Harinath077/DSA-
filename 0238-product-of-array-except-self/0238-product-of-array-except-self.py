class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroCnt = nums.count(0)
        n = len(nums)

        # case 1 : more than 1 zeros
        if zeroCnt > 1:
            return [0] * n
        
        # find continuous product
        product = 1
        for num in nums:
            if num == 0:
                continue
            product *= num
        
        ans = []

        # case 2 : only one zero 
        if zeroCnt == 1:
            for num in nums:
                if num == 0:
                    ans.append(product)
                else:
                    ans.append(0)
        else:
        # case 3 : no zero --> stright forward
            for num in nums:
                ans.append( product // num)
        
        return ans

