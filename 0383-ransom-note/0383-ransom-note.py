class Solution:
  def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    hash_map = dict()
    for letter in magazine:
      hash_map[letter] = hash_map.get(letter, 0) + 1
    
    for letter in ransomNote:
      if hash_map.get(letter, 0):
        hash_map[letter] -= 1
      else:
        return False
    
    return True
      