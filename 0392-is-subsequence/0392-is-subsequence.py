class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
      i = 0
      j = 0
      if s == "":
        return True
      while j < len(t):
        if s[i] == t[j]:
          i += 1
        if i == len(s):
          return True
        j += 1
      return False