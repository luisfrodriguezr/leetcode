class Solution:
  def containsDuplicate(self, nums: List[int]) -> bool:
    ans = False
    hash_set = dict()
    
    for num in nums:
      if num in hash_set:
        return True
      hash_set[num] = 1
    
    return False
        