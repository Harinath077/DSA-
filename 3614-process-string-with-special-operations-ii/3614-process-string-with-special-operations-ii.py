class Solution:
    def processStr(self, s: str, k: int) -> str:
        n = len(s)
        lens = [0] * (n + 1)

        LIMIT = 10**15 + 1

        for i, ch in enumerate(s):
            cur = lens[i]

            if 'a' <= ch <= 'z':
                lens[i + 1] = min(LIMIT, cur + 1)

            elif ch == '*':
                lens[i + 1] = max(0, cur - 1)

            elif ch == '#':
                lens[i + 1] = min(LIMIT, cur * 2)

            else:  # %
                lens[i + 1] = cur

        if k >= lens[n]:
            return '.'

        for i in range(n - 1, -1, -1):
            ch = s[i]

            if 'a' <= ch <= 'z':
                if k == lens[i + 1] - 1:
                    return ch

            elif ch == '#':
                k %= lens[i]

            elif ch == '%':
                if lens[i] > 0:
                    k = lens[i] - 1 - k

            else:  # '*'
                pass

        return '.'