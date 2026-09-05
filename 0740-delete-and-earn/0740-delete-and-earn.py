class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
      
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        arr = sorted(freq.keys())
        n = len(arr)

        dp = [0] * (n+1)

        for index in range(n-1, -1, -1):
            
            points = arr[index] * freq[arr[index]]

            # take 
            nextIndex = index + 1

            if nextIndex < n and arr[nextIndex] == arr[index] + 1:
                nextIndex += 1

            take = points + dp[nextIndex]

            notTake = dp[index + 1]

            dp[index] = max(take, notTake)

        return dp[0]
