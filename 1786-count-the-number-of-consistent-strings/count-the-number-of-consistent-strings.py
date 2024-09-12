class Solution:
  def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
    ans = 0
    hs = set()

    for c in allowed:
      hs.add(c)
    
    for word in words:
      consistent = True
      for c in word:
        if c not in hs:
          consistent = False
          break
      ans += consistent

    return ans
        