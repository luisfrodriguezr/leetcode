class Solution:
  def isCircularSentence(self, sentence: str) -> bool:
    if sentence[0] != sentence[-1]: return False
    for i, letter in enumerate(sentence):
      if letter == ' ':
        flag = True
        if sentence[i - 1] != sentence[i + 1]:
          return False
        
    return True
      
      
        