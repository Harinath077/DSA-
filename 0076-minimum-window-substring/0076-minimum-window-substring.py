class Solution:
    def minWindow(self, s: str, t: str) -> str:
        min_ = float("inf")
        n = len(s)
        m = len(t)
        mpp = defaultdict(int)
        count = 0
        index = -1
        for z in range(m):mpp[t[z]] += 1
        r , l =0,0
        while r < n:
            if mpp[s[r]] > 0:
                count += 1
            mpp[s[r]] -= 1
            while (count == m):
                if (r-l+1) < min_:
                    min_ = r-l+1
                    index = l
                mpp[s[l]] += 1
                if mpp[s[l]] > 0 :
                    count -= 1
                l += 1
            r += 1

        return "" if index == -1 else s[index:min_+index]
        