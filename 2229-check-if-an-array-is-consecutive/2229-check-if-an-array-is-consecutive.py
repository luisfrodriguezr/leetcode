class Solution:
  def isConsecutive(self, nums: List[int]) -> bool:
    hash_set = set()
    
    lower = 100001
    for num in nums:
      hash_set.add(num)
      lower = min(lower, num) 
    
    for i in range(lower, lower + len(nums)):
      if i not in hash_set:
        return False
    
    return True