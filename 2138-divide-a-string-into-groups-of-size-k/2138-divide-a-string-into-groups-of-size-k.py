class Solution:
  def divideString(self, s: str, k: int, fill: str) -> List[str]:
    ans = []
    
    for i in range(k, len(s) + 1, k):
      ans.append(s[i - k:i])
    
    if len(s) % k:
      ans.append(s[(len(s) // k) * k:] + fill * (ceil(len(s) / k ) * k - len(s)))
    
    return ans
      