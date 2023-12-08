class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
      words = text.split()
      ans = []
      for i, word in enumerate(words):
        if i > 1: #  Start Comparing from the 3 position
          if (words[i - 2] == first) and (words[i - 1] == second):
            ans.append(word)
      return ans
        