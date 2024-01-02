class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
      g = sorted(g)
      s = sorted(s)
      p1 = p2 = ans = 0
      while p1 < len(g) and p2 < len(s):
        if s[p2] >= g[p1]:
          ans += 1
          p1 += 1
        p2 += 1
      return ans
