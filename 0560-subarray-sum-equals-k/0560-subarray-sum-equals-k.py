class Solution:
  def subarraySum(self, nums: List[int], k: int) -> int:
    hash_map = {0: 1}
    curr = ans = 0
    for num in nums:
      curr += num
      if curr - k in hash_map:
        ans += hash_map[curr - k]
      hash_map[curr] = hash_map.get(curr, 0) + 1   
    return ans
      
      
      
        
      