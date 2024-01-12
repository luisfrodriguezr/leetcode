class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
      hashTable = [-1] * 26
      
      for i, c in enumerate(s):
        hash_key = ord(c) - ord('a')
        if hashTable[hash_key] > -1:
          if distance[hash_key] != i - hashTable[hash_key] - 1:
            return False
        hashTable[hash_key] = i
        
      return True
          
        