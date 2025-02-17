class Solution:
  def numSplits(self, s: str) -> int:
    ans = 0
    dp = [0] * len(s)
    curr = set()
  
    for i in range(len(s) - 1, -1, -1):
      curr.add(s[i])
      dp[i] = len(curr)
    
    curr = set()

    for i in range(len(s) - 1):
      curr.add(s[i])
      ans += len(curr) == dp[i + 1]
    
    return ans
       
    
        