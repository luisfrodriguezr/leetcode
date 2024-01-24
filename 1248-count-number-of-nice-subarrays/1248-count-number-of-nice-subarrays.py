class Solution:
  def numberOfSubarrays(self, nums: List[int], k: int) -> int:
    hash_map = {0: 1}
    curr = ans = 0
    
    for num in nums:
      curr += num % 2
      ans += hash_map.get(curr - k, 0)
      hash_map[curr] = hash_map.get(curr, 0) + 1
      
    return ans