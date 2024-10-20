class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    ans = 0

    dp = [0] * len(prices)
    maxRight = 0
    maxProfitRight = 0
    for i in range(len(prices) - 1, -1, -1):
      maxProfitRight = max(maxProfitRight, maxRight - prices[i])
      maxRight = max(maxRight, prices[i])
      dp[i] = maxProfitRight

    dp2 = [0] * len(prices)
    minLeft = 10 ** 5
    maxProfitLeft = 0
    for i in range(len(prices)):
      maxProfitLeft = max(maxProfitLeft, prices[i] - minLeft)
      minLeft = min(minLeft, prices[i])

      dp2[i] = maxProfitLeft

    for i in range(len(prices)):
      ans = max(ans, dp[i] + dp2[i])
    
    return ans


        