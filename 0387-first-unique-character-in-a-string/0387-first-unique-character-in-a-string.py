class Solution:
  def firstUniqChar(self, s: str) -> int:
    mp = dict()
    for c in s:
      mp[c] = mp.get(c, 0) + 1
    
    for i, c in enumerate(s):
      if mp[c] == 1:
        return i
    
    return -1
    