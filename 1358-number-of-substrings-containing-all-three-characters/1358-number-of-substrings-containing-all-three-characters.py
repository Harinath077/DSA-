class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = 0
        n = len(s)
        last_seen = [-1]*3
        for i in range(n):
            last_seen[ord(s[i]) - ord("a")] = i
            if -1 not in last_seen:
                count += min(last_seen)+1
        return count

        """
        brute Force
        count = 0
        n = len(s)
        for i in range(n):
            temp = []
            for j in range(i,n):
                temp.append(s[j])
                if all(i in temp for i in ["a","b","c"]):
                    count += 1
        return count
        """