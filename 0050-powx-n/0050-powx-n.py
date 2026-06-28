class Solution:
    def myPow(self, base: float, exponent: int) -> float:
        if exponent == 0:
            return 1.0
        if exponent < 0:
            base = 1 / base
            exponent = -exponent
        half = self.myPow(base,exponent//2)
        if exponent % 2:
            return half * half * base
        else:
            return half * half

        

        