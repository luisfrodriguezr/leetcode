class Solution:
  def findJudge(self, n: int, trust: List[List[int]]) -> int:
    if len(trust) == 0 and n == 1: return 1
    hash_map = dict()
    hash_set = set()
    
    for t in trust:
      hash_map[t[1]] = hash_map.get(t[1], 0) + 1
      hash_set.add(t[0])
    
    for k, v in hash_map.items():
      if v == n - 1 and k not in hash_set: return k
    
    return -1
        