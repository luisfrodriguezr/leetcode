class Solution:
  def divideArray(self, nums: List[int]) -> bool:
    hashMap = dict()
    
    for num in nums:
      hashMap[num] = hashMap.get(num, 0) + 1
      if hashMap[num] == 2:
        del hashMap[num]
    
    return not bool(len(hashMap))
        