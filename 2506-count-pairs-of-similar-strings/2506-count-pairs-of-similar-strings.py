class Solution:
    def similarPairs(self, words: List[str]) -> int:
      hash_map = dict()
      ans = 0
      
      for word in words:
        key = tuple(sorted(set(word)))
        hash_map[key] = hash_map.get(key, -1) + 1
        ans += hash_map[key]
      
      return ans
        