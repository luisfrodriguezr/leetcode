class Solution:
  def largestAltitude(self, gain: List[int]) -> int:
    ans = curr = 0
    for num in gain:
      curr += num
      ans = max(ans, curr)
    
    return ans