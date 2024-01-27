class Solution:
    def kInversePairs(self, n, k):
        M = 1000000007
        dp = [[0] * (k + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(k + 1):
                if j == 0:
                    dp[i][j] = 1
                else:
                    val = (dp[i - 1][j] + M - (dp[i - 1][j - i] if j - i >= 0 else 0)) % M
                    dp[i][j] = (dp[i][j - 1] + val) % M

        return (dp[n][k] + M - dp[n][k - 1]) % M if k > 0 else dp[n][k]