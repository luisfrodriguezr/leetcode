class Solution:
  def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
    hash_set_1 = set()
    hash_set_2 = set()
    
    for num in nums1:
      hash_set_1.add(num)
     
    for num in nums2:
      hash_set_2.add(num)
    
    
    for i in range(1, 10):
      if i in hash_set_1 and i in hash_set_2:
        return i
      
    d1 = d2 = 0  
    for i in range(9, 0, -1):
      if i in hash_set_1:
        d1 = i
      if i in hash_set_2:
        d2 = i
    
    return min(d1, d2) * 10 + max(d1, d2)