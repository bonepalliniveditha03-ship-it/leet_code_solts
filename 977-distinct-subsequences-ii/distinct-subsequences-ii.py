class Solution:
    def distinctSubseqII(self, s: str) -> int:
        Dp = [0] * 26
        mod = 10**9 + 7
        for ch in s:
            i = ord(ch)-ord('a')
            tot = sum(Dp) + 1
            Dp[i] = tot % mod
        return (sum(Dp)) % mod
        