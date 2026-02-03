class Solution:
    def prev_small_index(self,arr,n):
        ans = [0] * n
        stack = []
        for i in range(n):
            while( stack and arr[stack[-1]] > arr[i]):
                stack.pop()
            ans[i] = -1 if not stack else stack[-1]
            stack.append(i)
        return ans
    def next_small_index(self,arr,n):
            ans = [0]*n
            stack = []
            for i in reversed(range(n)):
                while( stack and arr[stack[-1]] >= arr[i]):
                    stack.pop()
                ans[i] = n if not stack else stack[-1]
                stack.append(i)
            return ans
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = int(1e9 + 7) 
        n = len(arr)
        prev = self.prev_small_index(arr,n)
        next_ = self.next_small_index(arr,n)

        total = 0
        for i in range(n):
            left = i - prev[i]
            right = next_[i] - i
            total = (total + (arr[i] * left * right) % MOD) % MOD
        return total

