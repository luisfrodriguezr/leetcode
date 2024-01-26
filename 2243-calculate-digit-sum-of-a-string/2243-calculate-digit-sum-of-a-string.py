class Solution:
  def digitSum(self, s: str, k: int) -> str:
    while len(s) > k:
      aux = 0
      string = []
      for i in range(1, len(s) + 1):
        aux += int(s[i - 1])
        if i % k == 0 or i == len(s):
          string.extend(list(str(aux)))
          aux = 0
      s = string.copy()
      l = len(s)
      pass
        
    return ''.join(s)
    
        