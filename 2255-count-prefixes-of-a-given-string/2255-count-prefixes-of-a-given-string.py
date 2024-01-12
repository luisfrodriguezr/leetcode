class Solution:
  def countPrefixes(self, words: List[str], s: str) -> int:
    ans = 0
    
    for word in words:
      ans += s.startswith(word)
    
    return ans
        
      
        