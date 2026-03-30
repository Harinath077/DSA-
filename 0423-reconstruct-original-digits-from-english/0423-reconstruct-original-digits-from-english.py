class Solution:
    def originalDigits(self, s: str) -> str:
        count = [0] * 26

        for ch in s:
            count[ord(ch) - ord('a')] += 1

        out = [0] * 10

        out[0] = count[ord('z') - ord('a')]
        out[2] = count[ord('w') - ord('a')]
        out[4] = count[ord('u') - ord('a')]
        out[6] = count[ord('x') - ord('a')]
        out[8] = count[ord('g') - ord('a')]

        out[3] = count[ord('h') - ord('a')] - out[8]
        out[5] = count[ord('f') - ord('a')] - out[4]
        out[7] = count[ord('s') - ord('a')] - out[6]
        out[1] = count[ord('o') - ord('a')] - out[0] - out[2] - out[4]
        out[9] = count[ord('i') - ord('a')] - out[5] - out[6] - out[8]

        res = ""
        for i in range(10):
            res += str(i) * out[i]

        return res