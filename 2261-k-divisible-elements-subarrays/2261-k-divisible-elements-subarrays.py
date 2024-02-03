class Solution:
  def countDistinct(self, nums: List[int], k: int, p: int) -> int:
    hs = set()
    curr = 0
    for i in range(len(nums)):
      curr += (nums[i] % p) == 0
      left = 0
      for j in range(0, i + 1):
        if curr - left <= k: hs.add(tuple(nums[j:i + 1]))
        left += (nums[j] % p) == 0
    
    return len(hs)
        
    
        
        