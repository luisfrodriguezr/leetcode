class Solution:
  def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    left = curr = 0
    ans = 100000 + 1
    
    for right in range(len(nums)):
      curr += nums[right]
      
      while True:
        curr -= nums[left]
        left += 1
        if curr < target:
          left -= 1
          curr += nums[left]
          break;
      
      if curr >= target:
        ans = min(ans, right - left + 1)
    
    if ans == 100001:
      return 0
    
    return ans
      
      
        