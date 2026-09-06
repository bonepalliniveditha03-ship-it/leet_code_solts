class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        Dp = [0] * (len(t) + 1)
        Dp[0] = 1

        for ch in s:
            for j in range(len(t), 0, -1):
                if ch == t[j - 1]:
                    Dp[j] += Dp[j - 1]

        return Dp[len(t)]

        