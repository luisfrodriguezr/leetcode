# Time complexity O(n * m)
# Space complecity O(1)
class Solution:
  def numberOfBeams(self, bank: List[str]) -> int:
    curr = prev = ans = 0
    for row in bank:
      if curr:
        prev = curr
        curr = 0
      for c in row:
        if c == '1':
          ans += prev
          curr += 1
    return ans
      