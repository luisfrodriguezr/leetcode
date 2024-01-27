class Solution:
  def destCity(self, paths: List[List[str]]) -> str:
    hash_map = dict()
    
    for path in paths:
      hash_map[path[0]] = hash_map.get(path[0], 0) + 1
      hash_map[path[1]] = hash_map.get(path[1], 0)
    
    for city in hash_map:
      if hash_map[city] == 0:
        return city
    