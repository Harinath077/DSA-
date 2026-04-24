class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        l = 0
        r = 0
        dash = 0
        for ch in moves:
            if( ch == 'L'):
                l += 1
            elif( ch == 'R'):
                r += 1
            else:
                dash += 1
        f = max(r,l)
        s = min(r,l)
        return  f-s + dash