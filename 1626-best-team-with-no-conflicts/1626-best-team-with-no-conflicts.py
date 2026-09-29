class Solution:
    def bestTeamScore(self, scores: list[int], ages: list[int]) -> int:
        @cache
        def dfs(index, prevAge):

            # base case
            if index == n:
                return 0
            
            if dp[index][prevAge+1] != -1:
                return dp[index][prevAge+1]

            notTake = dfs(index + 1, prevAge)

            take = 0
            if prevAge == -1 or players[index][1] >= players[prevAge][1]:
                take = players[index][1] + dfs(index + 1, index)
            
            dp[index][prevAge+1] = max(take,notTake)
            return dp[index][prevAge + 1]
        
        n = len(scores)
        players = []
        for i in range(n):
            players.append((ages[i], scores[i]))
        players.sort()

        dp = [[0] * (n+1) for _ in range(n+1)]

        for index in range(n-1, -1, -1):
            for prevAge in range(n-1, -2, -1):
                notTake = dp[index + 1][prevAge+1]

                take = 0
                if prevAge == -1 or players[index][1] >= players[prevAge][1]:
                    take = players[index][1] + dp[index + 1][index + 1]
                dp[index][prevAge+1] = max(take,notTake)

        return dp[0][0]