class Solution:
    def minTimeToType(self, word: str) -> int:
      ans = 0
      curr = 'a'
      for letter in word:
        ans += min(abs(ord(curr) - ord(letter)), abs(max(ord(curr), ord(letter)) - (min((ord(letter), ord(curr))) + 26)))
        curr = letter
      
      return ans + len(word)