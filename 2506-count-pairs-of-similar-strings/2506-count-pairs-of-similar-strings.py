class Solution:
    def similarPairs(self, words: List[str]) -> int:
      hash_map = dict()
      ans = 0
      
      for word in words:
        key = tuple(sorted(set(word)))
        hash_map[key] = hash_map.get(key, 0) + 1
      
      for value in hash_map.values():
        ans += int(value * (value - 1) / 2)
        
      return ans
        