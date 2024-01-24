class Solution:
  def findMaxLength(self, nums: List[int]) -> int:
    hash_map = {0: -1}
    curr = ans = 0
    for i, num in enumerate(nums):
      curr += 1 if num else -1
      
      if curr in hash_map:
        ans = max(ans, i - hash_map[curr])
      else:
        hash_map[curr] = i
    
    return ans
        