class Solution:
    """  
    helper(index) : return that vaild partition is available for nums[index : ]
    """
    def validPartition(self, nums: List[int]) -> bool:

        def isValid(arr):

            if len(arr) == 2:
                if arr[0] == arr[1]:
                    return True

            if len(arr) == 3:
                if arr[0] == arr[1] == arr[2]:
                    return True
                if arr[0] == arr[1]-1 and arr[1] == arr[2]-1:
                    return True

            return False
            
        n = len(nums)
        dp = [False] * (n + 1)

        # base case
        dp[n] = True

        for index in range(n-1, -1, -1):
            temp = []
            for j in range(index, min(index + 3, n)):
                temp.append(nums[j])
                if isValid(temp) and dp[j + 1]:
                    dp[index] = True
                    break

        return dp[0]