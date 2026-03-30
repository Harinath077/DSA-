class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def isValid(s):
            if len(s) > 1 and s[0] == '0':
                return False
            return int(s) <= 255

        def generateIpRec(s, index, curr, cnt, res):

            if index >= len(s):
                return

            # Validate last segment
            if cnt == 3:
                last = s[index:]
                if len(last) <= 3 and isValid(last):
                    res.append(curr + last)
                return

            segment = ""
            # Try segment length 1–3
            for i in range(index, min(index + 3, len(s))):
                segment += s[i]

                if isValid(segment):
                    generateIpRec(s, i + 1, curr + segment + ".", cnt + 1, res)


        res = []
        generateIpRec(s, 0, "", 0, res)
        return res