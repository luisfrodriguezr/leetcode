class Solution:
  def minBitFlips(self, start: int, goal: int) -> int:
    n = start ^ goal
    ans = 0

    while n:
      n, r = divmod(n, 2)
      ans += r
    
    return ans
        