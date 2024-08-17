class Solution:
  def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
    hs = set()
    
    for letter in brokenLetters:
      hs.add(letter)
    
    words = text.split(' ')
    ans = len(words)

    for word in words:
      for c in word:
        if c in hs:
          ans -= 1
          break
    
    return ans
      
        