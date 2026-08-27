class Solution:

  def lexGreaterPermutation(self, s: str, t: str) -> str:
    n = len(s)
    if len(t) != n:
      return ""

    # counts[c] represents (count in s) - (count in prefix of t)
    counts = [0] * 26
    for c in s:
      counts[ord(c) - ord("a")] += 1
    for c in t:
      counts[ord(c) - ord("a")] -= 1

    # Check if current counts contain any negative frequency
    def has_negative() -> bool:
      return any(c < 0 for c in counts)

    # Try matching prefix up to index i-1, and placing a strictly greater char at index i
    for i in range(n - 1, -1, -1):
      # Reclaim character t[i]
      counts[ord(t[i]) - ord("a")] += 1

      if has_negative():
        continue

      # Find the smallest available character strictly greater than t[i]
      t_val = ord(t[i]) - ord("a")
      best_j = -1
      for j in range(t_val + 1, 26):
        if counts[j] > 0:
          best_j = j
          break

      if best_j != -1:
        # Construct the result:
        # 1. Matching prefix t[0...i-1]
        # 2. Chosen character best_j
        # 3. Remaining characters sorted in ascending order
        ans = [t[:i], chr(ord("a") + best_j)]
        counts[best_j] -= 1

        for c_idx in range(26):
          if counts[c_idx] > 0:
            ans.append(chr(ord("a") + c_idx) * counts[c_idx])

        return "".join(ans)

    return ""