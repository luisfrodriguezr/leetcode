class Solution:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    hash_map = dict()
    
    for string in strs:
      key = tuple(sorted(string))
      if key not in hash_map:
        hash_map[key] = list()
      hash_map[key].append(string)
    
    return hash_map.values()