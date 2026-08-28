class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        
        players.sort()
        trainers.sort()

        n = len(players)
        m = len(trainers)

        p = 0
        t = 0

        while p < n and t < m:
            
            # certainly cannot train any subsequent stronger player
            if players[p] <= trainers[t]:
                p += 1
            # Discard this trainer and check the next one (t++).
            t += 1
        
        return p