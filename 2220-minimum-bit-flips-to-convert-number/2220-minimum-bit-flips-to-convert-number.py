class Solution:
  def minBitFlips(self, start: int, goal: int) -> int:
    target = start ^ goal
    ans = 0
    while target:
      ans += target % 2
      target //= 2
    
    return ans