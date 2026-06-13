class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        weightMap = dict(zip( alphabets, weights ))

        result = []

        for word in words:
            index = sum( weightMap[char] for char in word ) % 26
            result.append( chr(ord('z') - index) )
        return "".join(result)