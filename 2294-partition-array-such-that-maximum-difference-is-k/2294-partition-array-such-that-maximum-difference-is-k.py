class Solution:
  def partitionArray(self, nums: List[int], k: int) -> int:
    nums.sort(reverse=True)
    left = right = 0
    ans = 1
    while right < len(nums):
      if nums[left] - nums[right] > k:
        ans += 1
        left = right
      right += 1
    
    return ans
        