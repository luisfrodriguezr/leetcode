class Solution:
  def maximumValue(self, strs: List[str]) -> int:
    ans = 0
    
    for s in strs:
      x = 0

      if s.isnumeric():
        x = int(s)
      else:
        x = len(s)
      
      ans = max(ans, x)
    
    return ans
      
        