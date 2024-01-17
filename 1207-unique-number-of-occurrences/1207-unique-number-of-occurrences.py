class Solution:
  def uniqueOccurrences(self, arr: List[int]) -> bool:
    hashMap = dict()
    
    for num in arr:
      hashMap[num] = hashMap.get(num, 0) + 1
    
    hashMap_occ = dict()
    for key, value in hashMap.items():
      if hashMap_occ.get(value, 0) == 1: return False
      hashMap_occ[value] = 1
    
    return True
      
        