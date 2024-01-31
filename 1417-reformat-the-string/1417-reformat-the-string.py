class Solution:
    def reformat(self, s: str) -> str:
      ans = []
      digits = []
      letters = []
      def merge(l1, l2):
        for i in range(len(l1)):
          ans.append(l1[i])
          ans.append(l2[i])
      for c in s:
        if c.isdigit():
          digits.append(c)
        else:
          letters.append(c)
      
      if abs(len(digits) - len(letters)) > 1:
        return ""
      
      if len(digits) > len(letters):
        ans.append(digits.pop())
        merge(letters, digits)
      elif len(digits) < len(letters):
        ans.append(letters.pop())
        merge(digits, letters)
      else:
        merge(digits, letters)
      return ans