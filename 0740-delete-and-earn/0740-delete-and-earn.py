class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
    
        def dfs(index):
            # base case 
            if index >= n:
                return 0

            if memo[index] != -1:
                return memo[index]

            points = arr[index] * freq[arr[index]]

            # take 
            nextIndex = index + 1

            if nextIndex < n and arr[index]+1 == arr[nextIndex]:
                nextIndex += 1
            
            take = points + dfs(nextIndex)

            # not take
            notTake = dfs(index + 1)

            memo[index] = max(take, notTake)
            return memo[index]

      
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        arr = sorted(freq.keys())
        n = len(arr)

        memo = [-1] * n
        return dfs(0)
