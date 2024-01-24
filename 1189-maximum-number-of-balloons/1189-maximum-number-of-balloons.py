class Solution:
  def maxNumberOfBalloons(self, text: str) -> int:
    hash_map = dict()
    ans = 10001
    
    for c in text:
      add = 2 - int(c in 'lo')
      hash_map[c] = hash_map.get(c, 0) + add
    
    for c in 'balon':
      ans = min(ans, int(hash_map.get(c, 0)/2))
    
    return ans
      
        