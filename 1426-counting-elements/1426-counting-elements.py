class Solution:
  def countElements(self, arr: List[int]) -> int:
    hash_map = dict()
    
    for num in arr:
      hash_map[num] = hash_map.get(num, 0) + 1
    
    ans = 0
    for num in hash_map:
      if hash_map.get(num + 1, 0):
        ans += hash_map[num]
    
    return ans