class Solution:
  def checkIfPangram(self, sentence: str) -> bool:
    hashTable = [0] * 26
    
    for letter in sentence:
      hash_key = ord(letter) - ord('a')
      hashTable[hash_key] += 1
      
    for value in hashTable:
      if value == 0:
        return False
    
    return True
        