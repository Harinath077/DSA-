class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        seen_A = set()
        seen_B = set()
        common_count = 0
        result = []
        for i in range(n):
            if A[i] in seen_B:
                common_count += 1
            seen_A.add(A[i])

            if B[i] in seen_A:
                common_count += 1
            seen_B.add(B[i])
            result.append(common_count)
        return result
