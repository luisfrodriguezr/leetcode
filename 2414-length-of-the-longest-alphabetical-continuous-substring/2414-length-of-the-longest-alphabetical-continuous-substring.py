class Solution:
  def longestContinuousSubstring(self, s: str) -> int:
    left = ans = 0
    if len(s) == 1: return 1
    for right in range(1, len(s)):
      if ord(s[right - 1]) + 1 != ord(s[right]):
        ans = max(ans, right - left)
        left = right
      if right + 1 == len(s):
        ans = max(ans, right - left + 1)
    
    return ans
      
        