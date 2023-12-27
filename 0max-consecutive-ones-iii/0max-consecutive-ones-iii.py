class Solution:
  def longestOnes(self, nums: List[int], k: int) -> int:
    left = curr = ans = 0
    
    for right in range(len(nums)):
      # Count the number of 0's we want to keep it k at max
      if nums[right] == 0:
        curr += 1
      
      while curr > k:
        if nums[left] == 0:
          curr -= 1
        left += 1
      
      ans = max(ans, right - left + 1)
    
    return ans