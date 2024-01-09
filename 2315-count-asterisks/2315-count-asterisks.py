class Solution:
  def countAsterisks(self, s: str) -> int:
    flag = True
    ans = 0
    
    for c in s:
      if c == '|': flag = not flag
      if c == '*' and flag: ans += 1
        
    return ans
