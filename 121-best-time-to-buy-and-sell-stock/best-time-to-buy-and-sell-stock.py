class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    ans = 0
    mi = 10 ** 5 + 1

    for price in prices:
      mi = min(mi, price)
      ans = max(ans, price - mi)
    
    return ans

        