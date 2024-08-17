class Solution:
  def minimumKeypresses(self, s: str) -> int:
    hm, ans = dict(), 0
    repetitions = list()

    for c in s:
      hm[c] = hm.get(c, 0) + 1

    for _, value in hm.items():
      repetitions.append(value)
    
    repetitions.sort(reverse=True)
    
    for i, count in enumerate(repetitions):
      n = i // 9 + 1
      ans += count * n
    
    return ans
      
        