class Solution:
  def divideArray(self, nums: List[int]) -> bool:
    hashMap = dict()
    
    for num in nums:
      hashMap[num] = hashMap.get(num, 0) + 1
    
    for num in hashMap:
      if (hashMap[num] % 2):
        return False
      
    return True
        