class Solution:
  def freqAlphabets(self, s: str) -> str:
    hash_map = {str(i): chr(ord('a') + i - 1) for i in range(1, 10)}
    hash_map.update({str(i) + '#': chr(ord('a') + i - 1) for i in range(10, 27)})
    
    ans = list()
    
    i = len(s) - 1
    while i >= 0:
      if s[i] == '#':
        key = s[i - 2: i + 1]
        ans.append(hash_map[key])
        i -= 2
      else:
        ans.append(hash_map[s[i]])
      i -= 1
    
    return ''.join(reversed(ans))
      