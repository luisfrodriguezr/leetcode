class Solution:
  def numSquares(self, n: int) -> int:
    dp = [n] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
      for k in range(1, int(sqrt(n)) + 1):
        if i - (k * k) < 0: continue
        dp[i] = min(dp[i], dp[i - (k * k)] + 1)

    return dp[n]